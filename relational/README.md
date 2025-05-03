# Relational Databases

Relational databases are one of the most widely used and time-tested forms of data storage systems. They organize data into **tables (relations)** consisting of rows and columns, where each row represents a single record, and each column represents a specific attribute of that record.

## What Are Relational Databases?

A **Relational Database Management System (RDBMS)** uses structured schemas and relationships to enforce consistency and integrity across datasets. These systems are built on **relational algebra** and typically queried using **Structured Query Language (SQL)**.

Each table is designed to store information about a specific **entity** — which is a real-world object or concept.  
For example:
- A `users` table represents the **User** entity.
- A `transactions` table represents the **Transaction** entity.
- A `categories` table represents the **Category** entity.

An **entity** is typically mapped to a table, and its **attributes** (properties) are represented as columns.

Relationships between entities are maintained using **primary keys** (unique identifiers for each record) and **foreign keys** (references to primary keys in other tables).

This tabular design is ideal for applications where data integrity, normalization, and consistency are critical.

## Key Features

- **Structured Schema**: All data follows a fixed structure. Every row in a table has the same format, making it easy to manage.

- **Relationships via Keys**: Tables can be connected through foreign keys. This allows you to represent real-world relationships, like a one-to-many or many-to-many connection between tables.

- **SQL Query Language**: SQL is the most common language used to work with relational databases. It allows you to create, modify, and search for data easily.

- **Data Integrity & Constraints**: Features like unique constraints, foreign keys, and checks ensure that the data is correct and consistent across the database.

- **ACID Transactions**: Transactions are safe and work properly because of:
  - **Atomicity**: Either the whole transaction works, or nothing happens.
  - **Consistency**: The database stays correct before and after the transaction.
  - **Isolation**: Each transaction works on its own, without affecting others.
  - **Durability**: Once a transaction is done, it stays in the system even if something goes wrong.

## Advantages

- **Data Consistency**: Enforced by strong constraints and rules.
- **Mature Ecosystem**: Decades of development, optimization, and tooling.
- **Powerful Querying**: Advanced joins, aggregations, views, and stored procedures.
- **Integration Friendly**: Widely supported by most backend frameworks and ORM tools (like Django ORM, SQLAlchemy, Hibernate).

## ❌ Disadvantages

- **Fixed Schema**: Any schema change (e.g., adding/removing columns) can require careful migration planning.
- **Scalability Limits**: Vertical scaling is common, but horizontal scaling (sharding) is harder and often requires architectural adjustments.
- **Not Ideal for Semi/Unstructured Data**: JSON, media files, or polymorphic data structures are better handled by document stores or object databases.

## Common Use Cases

Relational databases are great when data needs to be well-organized and consistent. They are perfect for:

- Financial systems (e.g., banking, accounting, budgeting)
- Invoicing and ERP systems
- CRM and HRM platforms
- Booking and reservation systems
- Government and legal record systems

## Popular Relational Databases

Some of the most commonly used RDBMSs include:

- **PostgreSQL** – Open-source, powerful, and standards-compliant
- **MySQL / MariaDB** – Widely used in web hosting and LAMP stacks
- **SQLite** – Lightweight, embedded, and file-based
- **Microsoft SQL Server** – Enterprise-grade RDBMS from Microsoft
- **Oracle Database** – High-performance, feature-rich commercial RDBMS
