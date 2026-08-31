#-------AWS GLUE
# AWS GLUE is a serverless data integration and ETL service provided by AWS.

# it is mainly used to:
'''
Extract data
    ↓
Transform data
    ↓
Load data
'''

# Serverless ?
# User Do not need to create, configure, or manage his own server or spark cluster

# Instead of doing this:
'''
Create EC2 machines
      ↓
Install Spark
      ↓
Configure cluster
      ↓
Manage scaling
      ↓
Patch/maintain servers
      ↓
Run ETL
'''

# We do
'''
Upload/read data
      ↓
Write Glue/PySpark job
      ↓
Choose worker size
      ↓
Run job
'''

#-----Core Components

# 1. Glue Data Catalog
# Its main job is to store metadata about our Datasets. It does not store the actual data
'''
Actual data:
S3 → orders.csv

Metadata:
Glue Data Catalog
    ↓
Table: orders
    order_id     string
    customer_id  string
    price        double
    date         timestamp
'''
# 2. Glue Database
# It is a logical container for Data Catalog tables. Its main job is to group MetaData tables together.
'''
olist_ecommerce_db

├── raw_orders
├── raw_customers
├── raw_products
├── raw_payments
└── raw_reviews
'''
# 3. Glue Crawler
# A crawler Scans data sources and discovers its schema Automatically.
'''
S3
raw/orders/orders.csv
        ↓
Glue Crawler
        ↓
Reads header and sample data
        ↓
Detects schema
        ↓
Creates table
        ↓
Glue Data Catalog
'''
# it does not transform the actual data. it mainly discovers:
'''
Schema
Format
Columns
Data types
Partitions
Location
'''
# 4. Glue ETL Job
# This is where the actual transformation happens. Glue uses Apache Spark for Spark ETL jobs.
'''
S3 raw data
    ↓
Glue PySpark Job
    ↓
Remove duplicates
Handle null values
Cast data types
Join datasets
Apply business rules
Aggregate data
    ↓
S3 processed data
'''

#-------PYSPARK IN AWS GLUE
# AWS Glue supports PySpark, so we can use Spark DataFrames and Spark transformations.

# Example:
'''
df = spark.read.csv(
    "s3://bucket/raw/orders/",
    header=True,
    inferSchema=True
)
'''

# Type casting example:
'''
from pyspark.sql.functions import col

df = df.withColumn(
    "price",
    col("price").cast("double")
)
'''

# Writing output:
'''
df.write.mode("overwrite").parquet(
    "s3://bucket/processed/orders/"
)
'''

#-------DATAFRAME VS DYNAMICFRAME

# DataFrame
# Standard Apache Spark structure.
# Mostly used for:
'''
Joins
Window functions
Aggregations
Filtering
Spark SQL
Complex transformations
'''

# DynamicFrame
# AWS Glue specific structure.it is useful when data has schema changes or inconsistent structure.

# We can convert:
'''
DynamicFrame
      ↓
DataFrame
      ↓
Transformation
      ↓
DynamicFrame
'''
#-------GLUE CONNECTION
# Glue Connection stores connection details for external data sources.

# Mostly used with:
'''
RDS
PostgreSQL
MySQL
SQL Server
Redshift
Other JDBC sources
'''

# It may contain:
'''
JDBC URL
VPC
Subnet
Security Group
Credentials / Secrets
'''


#-------GLUE TRIGGER
# A Trigger starts a Glue job or crawler.

# Types:
'''
On-demand
Scheduled
Conditional
'''

# Example:
'''
Every day at 2 AM
      ↓
Trigger
      ↓
Glue Job
'''
#-------GLUE WORKFLOW
# Workflow is used to connect and control multiple Glue components.

'''
Crawler
   ↓
Raw Catalog Tables
   ↓
Glue ETL Job
   ↓
Processed Data
   ↓
Processed Crawler
   ↓
Athena
'''
#-------JOB BOOKMARK
# Job Bookmark helps Glue remember which data was already processed.

'''
Day 1:
100 files processed

Day 2:
5 new files arrive
'''

# Without bookmark:
'''
Process all 105 files again
'''

# With bookmark:
'''
Process only the 5 new files
'''

# Mainly used for incremental processing.

#-------GLUE DATA QUALITY
# AWS Glue can perform data quality checks.

'''
Null checks
Duplicate checks
Row count validation
Data type validation
Range checks
Uniqueness checks
Referential integrity
Freshness checks
Business rule validation
'''

# Example:
'''
order_id should not be NULL
price should be >= 0
order_id should be unique
customer_id should exist in customers
'''

# If critical checks fail:
'''
Fail the job
OR
Move bad records to quarantine
'''


#-------CSV TO PARQUET
# Glue is often used to convert CSV files into Parquet.

'''
CSV
 ↓
Glue
 ↓
Parquet
'''

# Parquet is better for analytics because:
'''
Columnar format
Compressed
Faster queries
Reads only required columns
Works well with Athena
Reduces scanned data
'''
#-------CLOUDWATCH
# CloudWatch is used to monitor Glue jobs.

# It gives:
'''
Job logs
Errors
Execution information
Metrics
Monitoring
'''

# If a Glue job fails:
'''
Glue Job Run
      ↓
CloudWatch Logs
'''


#-------GLUE STUDIO
# Glue Studio is the visual interface used to create and manage Glue ETL jobs.

'''
S3 Source
   ↓
Change Schema
   ↓
Filter
   ↓
Join
   ↓
S3 Target
'''

# We can also directly write our own PySpark script.


