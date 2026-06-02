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
  # DML : data manipulation language
   1. DML is used to manipulate data in tables
   2. DML is used to insert|delete|update data in tables
   **insert data in tables**

   ```
    insert into tablename (columnname1,columnname2,.....) values (value1,value2,.....);
    or
    insert into flip_payment values(null,1,'new',5000,12-05-2026,20-05-2026,'pending','yes');
    ```
   **delete data from tables**
    1. delete is used to delete all data from tables
    2. delete is used to delete particular data from tables
    3. delete is used to delete alternate date from tables
    4. delete is used to delete a range of data from tables
    5. after delete data from tables we can rollback data
    syntax:

    ```
     1. delete all date from tables
     delete from tablename;
     example:
     delete from flip_payment;
     2. delete particular data from tables
     delete from tablename where columnname=value;
     example:
     delete from flip_payment where payment_id=1;
     3. delete alternate data from tables
        delete from flip_payment where paymentid in (1,3,5);
     4. delet range of data from tables
     delete from flip_payment where paymentid between 1 and 5;

    ``` 
    **update data in tables**
    1. update any rows or data from tables
     1. syntax:
      ```
        update tablename set columnname=value where columnname=value;
        example:
        update flip_payment set payment_status='success' where payment_id=1;
      ```
  # DQL : data query language
    1. DQL is used to fetch data or select data from tables
    2. DQL is used to fetch all data| particular data| alternate data| range of data| limit of data
     from tables
    3. DQL is uses select.
    **examples all data from tables**
    1. select all data from tables
      syntax:
    ```
     select * from tablename;
     example:
     select * from flip_payment;
    ```
    2. select particular data from tables
    syntax:
    ```
     select columnname1,columnname2 from tablename;
     example:
     select payment_id,payment_status from flip_payment;
     select payment_id,payment_status from flip_payment where payment_status='pending';
    ```
    3. select ranege of data from tables
    syntax:
    ```
     select * from tablename where columnname between value1 and value2;
     example:
     select * from flip_payment where payment_id between 1 and 5;
    ```
    4. select alternate data from tables
    syntax:
    ```
     select * from tablename where columnname in (value1,value2,value3.....);
     example:
     select * from flip_payment where payment_id in (1,3,5);
    ```
    5. select data from tables using limit
    syntax:
    ```
     select * from tablename limit number;
     example:
     select * from flip_payment limit 2,5;
    ```
    **order by and group by**
  # order by 
   1. order by filter data from data from tables in ascending and descending order
   2. order by is used to sort data from tables in ascending and descending order
   **syntax**
   ```
    select * from tablename order by columnname asc|desc;
    example:
    select * from flip_payment order by payment_amount desc;
   ```
   # SQL Aggregate Functions
   1. SQL provides some built-in functions to perform operations on data
   **types**
   1. sum(): calculates the total sum of a numeric column.
   **syntax**
   ```
    select sum(columnname) from tablename;
    example:
    select sum(salary) from flip_employee;
   ```
   2. count(): counts the number of rows in a table or the number of non-null values in a column.
   **syntax**
   ```
    select count(columnname) from tablename;
    example:
    select count(*) from flip_employee;
   ```
    3. avg(): calculates the average value of a numeric column.
    **syntax**
    ```
     select avg(columnname) from tablename;
     example:
     select avg(salary) from flip_employee;
    ```
    4. max(): returns the maximum value in a column.
    **syntax**
    ```
     select max(columnname) from tablename;
     example:
     select max(salary) from flip_employee;
    ```
    5. min(): returns the minimum value in a column.
    **syntax**
    ```
     select min(columnname) from tablename;
     example:
     select min(salary) from flip_employee;
    ```
    6. alias: is used to give a temporary name to a column or table in a query result.
    **syntax**
    ```
     select columnname as aliasname from tablename;
     example:
     select salary as emp_salary from flip_employee;
    ```
  # SQL scalar functions
  1. first: returns the first value in a group of values.
  **syntax**
  ```
   select first(columnname) from tablename;
   example:
   select first(salary) from flip_employee;
  ```
  2. last: returns the last value in a group of values.
  **syntax**
  ```
   select last(columnname) from tablename;
   example:
   select last(salary) from flip_employee;
  ```
  3. ucase: converts a string to uppercase.
  **syntax**
  ```
   select ucase(columnname) from tablename;
   example:
   select ucase(name) from flip_employee;
  ```
  4. lcase: converts a string to lowercase.
  **syntax**
  ```
   select lcase(columnname) from tablename;
   example:
   select lcase(name) from flip_employee;
  ```
  # group by
   1. group by used to group data based on one or more columns
   2. group by is used with aggregate functions like COUNT, SUM, AVG, MAX, MIN
   **syntax**
   ```
    select columnname, aggregate_function(columnname) from tablename group by columnname;
    example:
    select payment_status, count(*) from flip_payment group by payment_status;
   ```
   **subquery**
    1. query within another query is called subquery.
    2. subquery is used to find second highest value from tables
    **syntax**
    ```
     select columnname from tablename where columnname operator (select columnname from tablename where condition);
     example:
     select max(amount) from flip_payment where amount< (select max(amount) from flip_payment);
     or 
     select amount from flip_payment order by amount desc limit 1,1;
     select amount from flip_payment order by amount desc limit 2,1;
    ```

  # like operator
   1. like operator is used to search for a specified pattern in a column.
   2. like operator is used with wildcard characters to match patterns in strings.
   **wildcard characters**
   1. % : represents zero or more characters
   2. _ : represents a single character
   3. [ ] : represents any single character within the brackets
   4. [^] : represents any single character not within the brackets
   5. - : represents a range of characters when used within brackets
   6. | : represents an OR condition when used within brackets
   7. \ : is used to escape special characters in the pattern
   8.$ : represents the end of a string
   9. ^ : represents the start of a string 
   10. () : is used to group patterns together
   **syntax**
   ```
    select * from tablename where columnname like pattern;
    example:
    select payment_status from flip_payment where payment_status like 'e%';
    select payment_status from flip_payment where payment_status like '%e';
    select payment_status from flip_payment where payment_status like '%e%';
    select payment_status from flip_payment where payment_status like '_e%';
   ```
