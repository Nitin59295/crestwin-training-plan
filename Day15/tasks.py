# Indexes :- An Index is used to make database searches faster.
# Instead of checking every row in a table, PostgreSQL can use the index
# to find the required data faster.

# Example:
# CREATE INDEX idx_students_name ON students(name);

# B-tree Index :- B-tree is the default and most commonly used index in PostgreSQL.
# It is useful for equality and range searches.

# Example:
# SELECT * FROM students
# WHERE name = 'Rahul';

# It is also useful for: age > 20, age < 30, age BETWEEN 20 AND 30

# When Indexes Improve Performance :- Indexes are useful when we have large tables and frequently search, filter, join or sort using a particular column.

# Example:
# SELECT * FROM students
# WHERE email = 'nitin@gmail.com';

# If email is indexed, PostgreSQL can find the record faster.


# Disadvantages of Indexes :- Indexes improve read performance but also have some disadvantages.

# - Indexes use extra storage.
# - INSERT can become slower because the index also needs to be updated.
# - UPDATE can become slower when indexed columns are changed.
# - DELETE also requires index maintenance.
# - Creating too many indexes can reduce write performance.


# EXPLAIN :- EXPLAIN shows how PostgreSQL plans to execute a query.

# Example:
# EXPLAIN
# SELECT * FROM students
# WHERE name = 'Rahul';


# EXPLAIN ANALYZE :- EXPLAIN ANALYZE actually executes the query
# and shows the real execution details.

# Example:
# EXPLAIN ANALYZE
# SELECT * FROM students
# WHERE name = 'Rahul';

# It can show:
# - Planning Time
# - Execution Time
# - Actual Rows
# - Scan Type


# Index Performance Example:

# Before creating index:
# EXPLAIN ANALYZE
# SELECT * FROM students
# WHERE name = 'Rahul';

# Create index:
# CREATE INDEX idx_students_name
# ON students(name);

# Run again:
# EXPLAIN ANALYZE
# SELECT * FROM students
# WHERE name = 'Rahul';

# Now we can compare the execution plan and execution time.


# ACID :- ACID properties help make database transactions reliable.

# A -> Atomicity
# C -> Consistency
# I -> Isolation
# D -> Durability


# Atomicity :- Either all operations in a transaction happen or none of them happen.

# Example:
# Transfer Rs.500 from Account A to Account B.
# Money should not be removed from A unless it can also be added to B.


# Consistency :- The database should remain in a valid state
# before and after the transaction.

# Example:
# If total money before transfer is Rs.10,000,
# total money should still be Rs.10,000 after the transfer.


# Isolation :- Multiple transactions should not incorrectly interfere with each other.

# Example:
# Two users are updating bank accounts at the same time.
# Their transactions should be handled safely.


# Durability :- Once a transaction is committed,
# the changes should remain saved.

# Example:
# If a payment is committed and the server crashes,
# the committed payment should still exist after restart.


# Transaction :- A Transaction is a group of database operations
# that are treated as one unit of work.


# BEGIN :- Starts a transaction.

# Example:
# BEGIN;


# COMMIT :- Saves all the changes made in the transaction.

# Example:
# BEGIN;
#
# UPDATE accounts
# SET balance = balance - 500
# WHERE id = 1;
#
# UPDATE accounts
# SET balance = balance + 500
# WHERE id = 2;
#
# COMMIT;


# ROLLBACK :- Cancels the changes made in the current transaction.

# Example:
# BEGIN;
#
# UPDATE accounts
SET balance = balance - 500
WHERE id = 1;
#
# Something goes wrong...
#
# ROLLBACK;

# The changes will not be saved.


# SQLAlchemy ORM :- ORM stands for Object Relational Mapping.
# It allows us to work with database tables using Python classes and objects.

# Instead of always writing:
INSERT INTO students ...

# We can work with:
Student(name="Nitin", age=22)


# DeclarativeBase :- DeclarativeBase is used as the base class
# for creating SQLAlchemy models.

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


# SQLAlchemy Model :- A model represents a database table.

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int]


# Here:
# Student -> Python class
# students -> Database table
# id, name, age -> Columns


# Session :- Session is used to communicate with the database. We use it to create, read, update and delete data.

# Example:
# from sqlalchemy.orm import Session
#
with Session(engine) as session:
    student = Student(name="Nitin", age=22)
    session.add(student)
    session.commit()


# SQLAlchemy CRUD :- CRUD stands for Create, Read, Update and Delete.


# CREATE :- Add new data.

# Example:
student = Student(name="Nitin", age=22)
session.add(student)
session.commit()


# READ :- Get data from the database.

# Example:
students = session.query(Student).all()


# UPDATE :- Modify existing data.

# Example:
student = session.query(Student).filter(Student.id == 1).first()
student.age = 23
session.commit()


# DELETE :- Remove data.

# Example:
student = session.query(Student).filter(Student.id == 1).first()
session.delete(student)
session.commit()


# Alembic :- Alembic is a database migration tool commonly used with SQLAlchemy. It helps us manage changes in the database structure.

# Migration :- A migration is a record of changes made to the database schema.

# Example:
Current students table:
id
name
age
#
# Now we add:
email
#
# Alembic can create a migration for this schema change.


# Initialize Alembic:

# alembic init alembic


# Create Migration:

# alembic revision --autogenerate -m "add email column"


# Upgrade :- Upgrade applies new migrations to the database.

# Example:
alembic upgrade head


# Downgrade :- Downgrade is used to revert a migration.

# Example:
alembic downgrade -1
