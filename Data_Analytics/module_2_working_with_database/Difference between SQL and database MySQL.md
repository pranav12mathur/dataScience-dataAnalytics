# what is SQL ?

SQL (Structured Query Language) is a standardized programming language used for managing and manipulating relational databases. It allows users to create, read, update, and delete data efficiently.

## Characteristics of SQL

 1. SQL is a structured query language 
 2. SQL is structured query based language 
 3. SQL is used to create a database and tables structured
 4. SQL will manage and provides relationship between tables  
 5. SQL is case-insensitive language
 6. SQL is most commonly used to create an structured database

## Advantages of SQL

 1. **Easy to Learn** - SQL has a simple and intuitive syntax that resembles English, making it easy for beginners to learn

 2. **Portability** - SQL works across different platforms and database systems (MySQL, PostgreSQL, Oracle, SQL Server, etc.)
 
 3. **High Performance** - SQL efficiently handles large volumes of data and performs complex queries quickly
 
 4. **Data Security** - SQL provides authentication and authorization mechanisms to protect sensitive data
 
 5. **ACID Compliance** - SQL supports transactions with ACID properties (Atomicity, Consistency, Isolation, Durability)
 
 6. **Data Integrity** - SQL enforces referential integrity and constraints to maintain data consistency
 
 7. **Standardized Language** - SQL follows standardized syntax across most relational database systems
 
 8. **Scalability** - SQL databases can handle growing volumes of data without performance degradation
 
 9. **Flexibility** - SQL supports complex queries and multiple data retrieval methods 


# SQL commands or query 

  1. SQL provides some query or commands 
  2. SQL is case - insenstive 
     examples : INSERT | insert | Insert
  3. best way to write query in small case 

  **types of SQL query**

  1. DDL (data definition language)
  2. DML (data manipulation language)
  3. DQL (data query language)
  4. TCL (Transactional query language)
 

 # mysql start database 

   1. xampp is a server tools 
      
      X -cross plateform(support all OS)
      A -apache (server)
      M -MySQL (database)
      P -Perl
      P -php

      **how to download xampp**

      ```
      https://www.apachefriends.org/ 

      ``` 

      ![alt text](image.png)
      
      localhost/phpmyadmin



# 2. mySQLworkBench2.0

      MySQLworkbench is also used for mysql database 
      MySQLworkbench is also used to create database | tables create 


**download and start**  

```
https://dev.mysql.com/downloads/file/?id=552199

```

# DDL (data definition language)

  1. DDL is used to create a database and table structured 
  2. DDL is also used to add | modify | rename any column name of table.
  3. DDL also drop and truncate a structures 
  4. DDL is also used to change the columnname of table 


  **examples of DDL**

  1. create 
  2. alter 
  3. rename 
  4. drop 
  5. change
  6. truncate   

**How to create a database structured**

 **syntax**

 ```
 create database databasename;
 or
 create database flipkart_shop;

 ```
  
**How to create a table structures**

**chart of table to create fieldname and datatype and its size in SQL**

```

| Data Type    | Description           | Example             |
| ------------ | --------------------- | ------------------- |
| INT          | Whole numbers         | 1, 100              |
| BIGINT       | Large whole numbers   | 999999999           |
| VARCHAR(n)   | Variable-length text  | VARCHAR(0-255)      |
| CHAR(n)      | Fixed-length text     | CHAR(1)             |
| TEXT         | Long text             | Paragraph           |
| DATE         | Date only             | 2026-05-25          |
| DATETIME     | Date + time           | 2026-05-25 10:30:00 |
| DECIMAL(p,s) | Exact decimal numbers | DECIMAL(10,2)       |
| FLOAT        | Decimal numbers       | 12.5                |
| BOOLEAN      | True/False            | TRUE                |
| BLOB         | Binary data/files     | Images/files        |
| ENUM         | select multiple choice| multiple choices    | 


```

**syntax to create a table in SQL**
```
create table tablename
(
  columnname1 datatype(size) auto_increment primary key,
  columnname2 datatype(size),
  .
  .
  .
  .
  .
)
```

**examples**

**create a employee tables**

```
create table employee
(
empid int primary key AUTO_INCREMENT,
name varchar(155),
password varchar(255),
email varchar(255),
phone bigint,
address text    
    
);
```

**create a reviews contact**

```
create table contact
(
contactid int primary key AUTO_INCREMENT,
name varchar(155),
email varchar(255),
subject ENUM('24x7 customer support','return product','customer care numbers'),
phone bigint,
message text    
    
);

```

**create a reviews tables**

```
create table reviews
(
reviewsid int primary key AUTO_INCREMENT,
name varchar(155),
email varchar(255),
ratings ENUM('1 star','2 star','3 star','4 star','5 star'),
phone bigint,
comment text    
    
);
```

**create a tables of products**

```
# Products Table Structure

| Column Name | Data Type | Size | Description |
|---|---|---|---|
| product_id | INT | 11 | Unique product ID |
| product_name | VARCHAR | 150 | Product name |
| product_code | VARCHAR | 50 | Product SKU/code |
| category_id | INT | 11 | Category reference ID |
| brand_name | VARCHAR | 100 | Brand name |
| price | DECIMAL | 10,2 | Product price |
| stock_quantity | INT | 11 | Available stock |
| weight | DECIMAL | 8,2 | Product weight |
| color | VARCHAR | 50 | Product color |
| size | VARCHAR | 20 | Product size |
| description | TEXT | Large Text | Product description |
| image_url | VARCHAR | 255 | Product image path/url |
| is_active | BOOLEAN | — | Product active status |
| created_at | DATETIME | — | Record creation time |
| updated_at | DATETIME | — | Last updated time |

```

# SQL Create Table Query

 ```
 CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(150) NOT NULL,
    product_code VARCHAR(50) UNIQUE,
    category_id INT,
    brand_name VARCHAR(100),
    price DECIMAL(10,2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    weight DECIMAL(8,2),
    color VARCHAR(50),
    size VARCHAR(20),
    description TEXT,
    image_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
  );

```

# alter 
  1. alter is used to add new columns in tables
  2. alter is used to modify or change  columns name in tables
  3. alter is used to drop  columns name in tables

 ```
  alter is used to add | modify | update | drop a columns from table 
  
  1. alter table employee add added_date date;
  2. alter table employee add is_Active boolean DEFAULT TRUE;
  3. alter table employee add photo blob after email;
  4. alter table employee CHANGE name employeename varchar(255)
  5. alter table employee drop photo;

 ```


# rename : after create tables we rename the tables name

  ```
  rename table reviews to flip_reviews

  ```


# drop : is drop database and tables both after drop we can not rollback anything 

  **drop database**

  ```
 
   drop database databasename;
   
   or

   drop database flipkart_shop
 
  ```

  **drop table**

  ```
 
   drop table tablename;
   
   or

   drop table flip_contact
 
  ```


# truncate : 

  1. truncate is used to delete data only from tables 
  2. truncate is also used to empty tables rows 
  3. after truncate data from tables we can not rollback data 

  ```
   truncate table tablename;
   or
   truncate table flip_reviews;
   
  ``` 