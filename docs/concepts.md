# Concepts

> Key concepts introduced in this module.

<!--
Only the first sentence/paragraph of h3 entries
are used for the integrated quiz.

Wrap code terms in double asterisks
rather than single backticks so they can be read aloud.
-->

## 1. Databases and SQL

### Database

A **database** is an organized collection of data designed for
reliable storage, retrieval, and management.

Databases are useful when data must be stored persistently,
queried efficiently, updated, shared, or related to other data.

### Relational database

A **relational database** organizes data primarily
into tables with rows and columns.

Relationships between tables allow related information to be
stored separately and combined when needed.

### SQL

**SQL**, or Structured Query Language, is a language used to
work with relational databases.

Analysts use SQL to select, filter, sort, combine, summarize,
insert, update, and delete data.

### When to use SQL

SQL is especially useful when data is stored in relational tables
and the goal is to retrieve, combine, filter, or summarize selected data.

Often it is better to ask the database for the needed data
than to load everything into another tool first.

## 2. Relational Data

### Table

A **table** stores related data in rows and columns.

Each column describes one kind of information, and each row represents one record.

### Data type

A **data type** describes the kind of values a database column is designed to store.

Choosing an appropriate type helps the database represent, validate,
store, and work with the data correctly.

### Key

A **key** is a column or set of columns used to
identify records or connect related tables.

Keys are important because relationships between tables
depend on knowing which records belong together.

### NULL

**NULL** represents a missing or unknown database value.

NULL is different from zero, an empty string,
or another value used as a placeholder for missing data.

## 3. Querying Data

### Query

A **query** is a request for data or an instruction sent to a database.

A SQL query can retrieve existing data or
perform operations that change stored data.

### Filtering and sorting

SQL can **filter** rows to keep records that meet c
onditions and **sort** results into a useful order.

Commands such as **WHERE** and **ORDER BY** help analysts
focus on the data needed for a question.

### DISTINCT

**DISTINCT** removes duplicate values from the results of a SQL query.

It is useful when the goal is to identify the different values
that occur rather than every occurrence.

### Join

A **join** combines related rows from two or more tables using matching values.

Different types of joins determine whether unmatched records are included or excluded.

### Aggregation and grouping

**Aggregation** summarizes many rows into values such as counts, totals, or averages.

SQL can use **GROUP BY** to calculate these summaries separately for different groups.

## 4. Changing and Checking Data

### Insert, update, and delete

SQL can **insert** new records, **update** existing records, and **delete** records.

These commands change stored data, so they should be
used deliberately and verified carefully.

### Data quality

**Data quality** describes whether data is suitable for its intended use.

Analysts look for issues such as missing values, unexpected values,
duplicates, inconsistent representations, and incorrect relationships.

## 5. Database Systems

### MySQL

**MySQL** is a relational database management system that uses SQL.

It provides software for storing relational data and
executing SQL commands against that data.

### PostgreSQL

**PostgreSQL** is a relational database management system that uses SQL.

MySQL and PostgreSQL support the same core relational
and SQL concepts, although their features and SQL syntax can differ in some areas.

### MongoDB

**MongoDB** is a document-oriented database rather than a relational database.

Instead of organizing data primarily into relational tables,
MongoDB stores document-like records that can contain nested structures.

### Choosing a database tool

The best database tool depends on the structure of the data
and how the data needs to be stored, related, queried, and changed.

Relational systems such as MySQL and PostgreSQL are
strong choices for structured data with important relationships,
while document databases such as MongoDB
can be useful when records have more flexible or nested structures.

---

[◄ Back to Home](index.md)
