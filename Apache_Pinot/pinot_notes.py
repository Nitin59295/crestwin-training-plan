#-------------------------------------------------------------------------------
# Apache Pinot - Engineering Notes & Production Runbook
# Author: Data Engineering Intern
# Topic: Apache Pinot internals, Spark ingestion, and troubleshooting guide

import json
from datetime import datetime

#----------------What is Apache Pinot (in simple terms):
# Think of Apache Pinot as a super fast database made for real-time dashboards.
# If Postgres is good for single-row updates (like changing user address)
# and Hive/Snowflake is good for scanning years of old history (takes minutes),
# Pinot is built for one specific job:
# Running analytical queries (SUM, COUNT, GROUP BY, WHERE filters)
# on millions of fresh incoming records in under 50 milliseconds.
#
# Created by LinkedIn for features like "Who viewed your profile" and ad analytics.
# Now used by Uber, Stripe, Walmart, etc.


#----------------Comparison: When to use Pinot vs other databases:
# 1. PostgreSQL / MySQL:
#    - Good for: OLTP, user accounts, transactions, single record CRUD.
#    - Problem: Slow when doing GROUP BY or COUNT over 50M+ rows.
#
# 2. Apache Hive / Trino / Snowflake:
#    - Good for: Heavy batch analytics, daily/monthly reports, joining big tables.
#    - Problem: High query latency (5s to a few minutes). Not suitable for UI dashboards.
#
# 3. Elasticsearch:
#    - Good for: Text search, log search, unstructured documents.
#    - Problem: High memory and CPU cost when doing pure numerical aggregations at scale.
#
# 4. Apache Pinot:
#    - Good for: Fast aggregates (SUM, AVG, COUNT, GROUP BY) on live streaming data with <50ms response.
#    - Problem: No ACID transactions, updates are expensive, complex multi-table joins are limited.


#----------------Pinot Architecture - Main Components:
# 1. Controller:
#    - Master manager of the cluster.
#    - Manages schemas, table configs, segment assignments across servers.
#    - Coordinates with ZooKeeper and Helix.
#
# 2. Broker:
#    - Query entry point for dashboards/APIs.
#    - Receives SQL query, figures out which servers hold the segments,
#      scatters the query to those servers, merges partial answers, and returns JSON.
#
# 3. Server:
#    - The worker node that stores the actual data chunks (Segments).
#    - Runs filters and calculations locally on its segments.
#
# 4. Segments:
#    - Consuming Segment: Mutable data chunk sitting in RAM taking in fresh data right now.
#    - Sealed Segment: Immutable, compressed, indexed file stored on disk and deep storage (S3/HDFS).


#----------------Why is Pinot so fast:
# 1. Columnar Storage (Forward Index):
#    Instead of reading full rows, Pinot reads only the specific columns needed in the query.
#
# 2. Inverted Index (Dictionary / Bitmaps):
#    Like an index at the back of a book.
#    Maps values to row IDs (e.g. status 'PLACED' -> [0, 4, 12, 19]).
#    Pinot jumps straight to matching rows instead of scanning everything.
#
# 3. Star-Tree Index:
#    Pre-calculates aggregations (like SUM(amount) by product) during ingestion time.


#----------------What happens when Spark sends data to Pinot (Step by step):
# Step 1: Spark cleans and validates a batch of records.
# Step 2: Spark Pinot connector sends the batch to the Pinot cluster.
# Step 3: Pinot checks schema (validates dimension, metric, and timestamp fields).
# Step 4: Pinot writes records into an in-memory "Consuming Segment".
#         Records are queryable in RAM immediately (<5ms).
# Step 5: Pinot builds forward indexes and inverted indexes.
# Step 6: When segment reaches size limit (e.g. 500k rows or 2 hours), it gets "Sealed".
# Step 7: Sealed segment is compressed and backed up to Deep Storage (S3 / HDFS).
# Step 8: A new empty consuming segment starts accepting new records.


#----------------Pinot Schema Example:
pinot_schema = {
    "schemaName": "orders_realtime",
    "dimensionFieldSpecs": [
        {"name": "order_id", "dataType": "STRING"},
        {"name": "customer_id", "dataType": "STRING"},
        {"name": "product", "dataType": "STRING"},
        {"name": "status", "dataType": "STRING"}
    ],
    "metricFieldSpecs": [
        {"name": "amount", "dataType": "DOUBLE"}
    ],
    "dateTimeFieldSpecs": [
        {
            "name": "event_time",
            "dataType": "TIMESTAMP",
            "format": "1:MILLISECONDS:EPOCH",
            "granularity": "1:MILLISECONDS"
        }
    ]
}


#----------------Pinot Table Config Example:
pinot_table_config = {
    "tableName": "orders_realtime",
    "tableType": "REALTIME",
    "segmentsConfig": {
        "timeColumnName": "event_time",
        "schemaName": "orders_realtime",
        "replication": "2",
        "retentionTimeUnit": "DAYS",
        "retentionTimeValue": "7"
    },
    "tableIndexConfig": {
        "invertedIndexColumns": ["product", "status"],
        "loadMode": "MMAP"
    }
}


#----------------Scenario 1: Query Latency Spikes (Dashboard suddenly takes 3-5 seconds):
# 1. Comparison:
#    - Expected: Aggregate queries on 'orders_realtime' return in <50ms.
#    - Problem: Queries taking 3 to 5 seconds, causing timeouts on the UI dashboard.
#
# 2. Where to look:
#    - Pinot Query Console (http://<broker-host>:9000/#/query)
#    - Broker logs (/var/log/pinot/pinot-broker.log)
#    - Server logs (/var/log/pinot/pinot-server.log)
#
# 3. What to look for:
#    - In query stats response, check "numDocsScanned" vs "totalDocs".
#      If numDocsScanned equals totalDocs, Pinot is doing a slow full table scan.
#    - Check if the column used in the WHERE filter is missing from "invertedIndexColumns".
#
# 4. How to fix:
#    - Add the filtered column into "invertedIndexColumns" in tableConfig.json.
#    - Trigger index reload via Pinot Controller API:
#      POST /tables/orders_realtime/rebuildIndex
#    - If doing heavy multi-column GROUP BY, enable Star-Tree index in table config.


#----------------Scenario 2: Data Freshness Lag (Dashboard is 15-20 minutes behind Kafka):
# 1. Comparison:
#    - Expected: Events from Kafka show up in Pinot within 1-2 seconds.
#    - Problem: Dashboard is showing data with a 15 to 30 minute delay.
#
# 2. Where to look:
#    - Kafka consumer lag dashboard (Grafana / Burrow)
#    - Spark Streaming UI (http://<spark-driver>:4040/streaming)
#    - Pinot Controller UI (http://<controller-host>:9000/#/tables)
#
# 3. What to look for:
#    - Kafka lag count growing continuously.
#    - In Spark UI: "Batch Processing Time" is higher than "Batch Interval" (e.g. taking 10s to process a 2s batch).
#    - In Pinot Controller: Check if any consuming segment is in ERROR or OFFLINE state.
#
# 4. How to fix:
#    - If Spark is slow: Scale up Spark executors (spark.executor.instances) or increase Kafka partitions.
#    - If Pinot consuming segment is stuck: Reset/restart the segment from Pinot Controller UI.
#    - Check if garbage collection (GC) pauses are happening on Spark or Pinot server JVM.


#----------------Scenario 3: Spark Job Fails Ingestion (SchemaMismatchException):
# 1. Comparison:
#    - Expected: Spark micro-batch writes cleaned data into Pinot without errors.
#    - Problem: Spark streaming job crashes with SchemaMismatchException or bad records dropped.
#
# 2. Where to look:
#    - Spark executor logs / stderr
#    - Pinot Controller logs (/var/log/pinot/pinot-controller.log)
#    - Pinot Schema via API: GET /schemas/orders_realtime
#
# 3. What to look for:
#    - Check for data type mismatches (e.g. Spark sends DoubleType, but Pinot schema defined amount as INT).
#    - Check if upstream team added a new column to JSON that is missing in Pinot schema.
#    - Check timestamp unit: epoch milliseconds vs seconds.
#
# 4. How to fix:
#    - Update Pinot schema using Controller API (PUT /schemas/orders_realtime) to add new fields.
#    - In PySpark, explicitly cast fields before writing:
#      df = df.withColumn("amount", col("amount").cast("double"))
#    - If schema change is breaking, create a new table version and replay offsets.


#----------------Scenario 4: Pinot Server Out of Memory (OOM) Crash:
# 1. Comparison:
#    - Expected: Pinot servers run with steady heap memory (~60-70%).
#    - Problem: Pinot Server JVM crashes with java.lang.OutOfMemoryError: Java heap space.
#
# 2. Where to look:
#    - Pinot Server logs and GC logs (/var/log/pinot/gc.log)
#    - Linux dmesg logs for OOM killer messages
#    - Table config file (tableConfig.json)
#
# 3. What to look for:
#    - Users running huge queries without LIMIT (e.g. SELECT * FROM orders_realtime).
#    - Missing retention config: if retentionTimeValue is not set, old segments stay on disk/RAM forever.
#    - Segment flush threshold set too high (e.g. 10M rows in a single consuming segment).
#
# 4. How to fix:
#    - Enforce broker query limit: pinot.broker.query.response.limit=1000.
#    - Add retention policy in tableConfig (e.g. retentionTimeValue: "7", retentionTimeUnit: "DAYS").
#    - Lower segment threshold: realtime.segment.flush.threshold.rows=500000.
#    - Increase JVM heap (-Xms16g -Xmx16g) and ensure off-heap MMAP memory is available.


#----------------Quick Interview Summary:
# Q: What is Apache Pinot in 1 line?
# A: A real-time distributed OLAP datastore built for sub-second analytical queries on fresh data.
#
# Q: Why Pinot instead of Hive?
# A: Hive is for batch queries on cold data (takes seconds to minutes).
#    Pinot is for real-time serving on hot data (takes 10-50ms).
#
# Q: What makes Pinot fast?
# A: Columnar format, inverted index bitmaps, dictionary encoding, and Star-Tree indexing.

if __name__ == "__main__":
    print("Apache Pinot Reference Notes & Troubleshooting Runbook")
    print("Schema preview:")
    print(json.dumps(pinot_schema, indent=2))
