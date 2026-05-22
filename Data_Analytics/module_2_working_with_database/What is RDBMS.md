# What is RDBMS?

RDBMS (Relational Database Management System) is a type of database management system that stores data in structured tables (rows and columns) and manages relationships between those tables using keys.

Key concepts
- Tables: collections of rows (records) and columns (fields).
- Schema: the structure that defines tables, columns, data types, and constraints.
- Primary key: a column or set of columns that uniquely identify a row.
- Foreign key: a column that creates a relationship between tables by referencing a primary key in another table.
- Indexes: data structures that speed up queries on specified columns.

Core properties
- ACID transactions: Atomicity, Consistency, Isolation, Durability ensure reliable transaction processing.
- SQL (Structured Query Language): the standard language for querying and managing relational databases.
- Normalization: process of organizing data to reduce redundancy and improve integrity (1NF, 2NF, 3NF, etc.).

Common features
- Referential integrity enforced via constraints (primary/foreign keys).
- Joins to combine data from multiple tables (INNER, LEFT, RIGHT, FULL).
- Views, stored procedures, triggers, and transactions.

Advantages
- Strong data integrity and consistency.
- Powerful query capabilities with SQL.
- Mature tooling, backup, and security features.

Limitations
- Can be less suitable for highly unstructured or extremely large-scale distributed data without sharding or specialized architectures.
- Vertical scaling sometimes required for very write-heavy workloads.

Popular RDBMS examples
- MySQL, PostgreSQL, Microsoft SQL Server, Oracle Database, SQLite.

When to use
- Structured data with clear schema and relationships.
- Applications requiring transactions, data integrity, and complex queries (finance, ERP, inventory, CRM).

Basic SQL examples
- Create table:
	CREATE TABLE customers (id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100));
- Insert:
	INSERT INTO customers (id, name, email) VALUES (1, 'Alice', 'alice@example.com');
- Query with join:
	SELECT o.id, c.name FROM orders o JOIN customers c ON o.customer_id = c.id;

Further topics to explore
- Query optimization, indexing strategies, normalization vs denormalization, replication, sharding, and cloud-managed RDBMS services.
