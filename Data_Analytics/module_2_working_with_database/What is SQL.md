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
  # key constraints in SQL ......

 1. key constraints are used to provide a limitation on a  tables 
 2. key constraints are ...

    1. primary key 
    2. unique key 
    3. foreign key  

# primary key :

1. A pk key never return a null values 
2. A pk key always have an auto_increments 
3. A pk will provides only one times in tables
4. A pk stored a unique values 

**create table with pk**

create table reviews ( reviewsid int primary key AUTO_INCREMENT, name varchar(155), email varchar(255), ratings ENUM('1 star','2 star','3 star','4 star','5 star'), phone bigint, comment text

);


**create in md formate**

# Reviews Table Structure

| Column Name | Data Type | Size / Values | Constraints |
|------------|-----------|---------------|-------------|
| reviewsid | INT | - | PRIMARY KEY, AUTO_INCREMENT |
| name | VARCHAR | 155 | NULL Allowed |
| email | VARCHAR | 255 | NULL Allowed |
| ratings | ENUM | '1 star', '2 star', '3 star', '4 star', '5 star' | NULL Allowed |
| phone | BIGINT | - | NULL Allowed |
| comment | TEXT | Large Text | NULL Allowed |


# unique key :
 
  1. A uk key return one times a null value   
  2. A uk will provides many times in a tables on columns
  3. A uk stored a unique values
  4. A uk never stored an dublicate values in tables 
  
**create table with uk**

ALTER TABLE flip_register ADD UNIQUE(email); or ALTER TABLE flip_register ADD UNIQUE(phone);

  
**note : here email and phone are unique key set and it is never stored a dublicate values**  

# foreign key :
    
  1. A fk will provides many times in a tables on columns with common field or column
  3. A fk are used to provides an relationship b/w one table to another table
  4. A fk can stored an dublicate key with common field

**create table with fk**

# create a flip_country table

create table flip_country ( cid int AUTO_INCREMENT primary key, countryname varchar(255)
)


# create a flip_users table 

create table flip_users ( uid int AUTO_INCREMENT primary key, name varchar(255), email varchar(255), phone bigint, cid int REFERENCES flip_country(cid)
)

# create an tables with foreign key ....

# ecommerce managements

1. flip_category
  ```
    CREATE TABLE flip_category (
    catid INT AUTO_INCREMENT PRIMARY KEY,
    categoryname VARCHAR(255)
  ) ENGINE=InnoDB; 
  ```        
2. flip_subcategory
  ```
    CREATE TABLE flip_subcategory (
    subcatid INT AUTO_INCREMENT PRIMARY KEY,
    catid INT NOT NULL,
    subcategoryname VARCHAR(255),
    CONSTRAINT fk_subcategory_category
    FOREIGN KEY (catid) REFERENCES flip_category(catid)
  ) ENGINE=InnoDB; 
  ```
3. flip_products
  ```
    CREATE TABLE flip_product (
    productid INT AUTO_INCREMENT PRIMARY KEY,
    catid INT NOT NULL,
    subcatid INT NOT NULL,
    productname VARCHAR(255) NOT NULL,
    brand VARCHAR(100),
    price DECIMAL(10,2),
    stock INT,
    description TEXT,
    productimage VARCHAR(255),

    CONSTRAINT fk_product_category
    FOREIGN KEY (catid) REFERENCES flip_category(catid),

    CONSTRAINT fk_product_subcategory
    FOREIGN KEY (subcatid) REFERENCES flip_subcategory(subcatid)
  ) ENGINE=InnoDB;  
  ``` 

# students managements 

1. flip_courses
  ```
     create table flip_courses
     (
         courseid int AUTO_INCREMENT primary key,
         coursename varchar(255)
     ) ENGINE=InnoDB;
  ```
2. flip_faculty
  ```
     create table flip_faculty
     (
         fid int AUTO_INCREMENT primary key,
         facultyname varchar(255),
         constraint fk_faculty_course
         foreign key (fid) references flip_courses(courseid)
     ) ENGINE=InnoDB;
  ```
1. flip_students
  ```
     create table flip_students
     (
        sid int AUTO_INCREMENT primary key,
        studentname varchar(255),
        email varchar(255),
        constraint fk_student_course
        foreign key (sid) references flip_courses(courseid)
        constraint fk_student_faculty
        foreign key (sid) references flip_faculty(fid)
     ) ENGINE=InnoDB;
  ```
# task managements 

1. flip_priority
  ```
      create table flip_priority
      (
          priorityid int AUTO_INCREMENT primary key,
          priorityname varchar(255)
      ) ENGINE=InnoDB;
  ```
2. flip_employee 
  ```
      create table flip_employee
      (
          empid int AUTO_INCREMENT primary key,
          empname varchar(255),
          email varchar(255),
          phone bigint,
          constraint fk_employee_priority
          foreign key (empid) references flip_priority(priorityid)
      ) ENGINE=InnoDB;
  ```
3. flip_task
  ```
      create table flip_task
      (
          taskid int AUTO_INCREMENT primary key,
          taskname varchar(255),
          description text,
          empid int,
          constraint fk_task_priority
          foreign key (empid) references flip_priority(priorityid),
          constraint fk_task_employee
          foreign key (empid) references flip_employee(empid)
      ) ENGINE=InnoDB;
  ```


# SQL join
  command used to combine rows from two or more tables based on a related column between them.
  ```
    example:
    select * from flip_task t
    join flip_employee e on t.empid = e.empid
  ```


# user management system
 1. country
  ```
    create table flip_country
    (
        country_id int AUTO_INCREMENT primary key,
        country_name varchar(255)
    )
  ```
 2. state
  ```
    create table flip_state
    (
        state_id int AUTO_INCREMENT primary key,
        state_name varchar(255)
    )
  ```
  
 3. city
  ```
    create table flip_city
    (
        city_id int AUTO_INCREMENT primary key,
        city_name varchar(255)
    )
  ```
 4. users
  ```
     create table users
      (
          user_id int AUTO_INCREMENT primary key,
          user_name varchar(255),
          user_salary decimal(10,2),
          user_age int,
          country_id int references flip_country(country_id),
          state_id int references flip_state(state_id),
          city_id int references flip_city(city_id)
      )
  ```

 # question
 1. select only country name from country table in uppercase
 2. select only state name from state table in uppercase
 3. select only city name from city table in uppercase
 4. select uid,uname,salary,countryname,statename,cityname from users table to get all name of country, state and city
 ## note: create users table with normalisation and provides cid,sid, and ctid as foreign key
 # answers
  1. select ucase(country_name) from flip_country;
  2. select ucase(state_name) from flip_state;
  3. select ucase(city_name) from flip_city;
  4. select u.user_id, u.user_name, u.user_salary, c.country_name, s.state_name, ci.city_name
     from flip_users u
     join flip_country c on u.country_id = c.country_id
     join flip_state s on u.state_id = s.state_id
     join flip_city ci on u.city_id = ci.city_id;

# Types of join in SQL
 1. join
 2. inner join
 3. left join
 4. right join
 5. full outer join
 6. cross join
 # What is join?
   1. join is used to join more than one coloumns data with common field or column if data matched one table to another
   **department**
| dept_id | dept_name |
|---------|-----------|
| 1       | IT        |
| 2       | CSE       |
| 3       | HR        |
| 4       | Finance   |

**employee**
| emp_id | emp_name | age | salary | dept_id(fk) |
|--------|----------|-----|--------|-------------|
| 1      | John     | 30  | 50000  | 1           |
| 2      | Jane     | 28  | 60000  | 2           |
| 3      | Mike     | 35  | 55000  | 1           |
| 4      | Sarah    | 32  | 65000  | 2           |
| 5      | David    | 29  | 52000  | 1           |
| 6      | Emily    | 31  | 62000  | 2           |

# Question 1: write a SQL query to create departments tables and insert 4 rows
# Question 2: write a SQL query to fetch only department name in uppercase
# Question 3: write a SQL query to fetch only department name in descending order
# Question 4: write a SQL query to fetch employee details whose salary is second highest
# Question 5: write a SQL query to fetch only details of emp_id 3,5,2 employee details
# Question 6: write a SQL query to fetch only employee details whose name start with 'f' character
# Question 7: write a SQL query to fetch department name inside of employee details with join query


# answers
1. create table flip_department(
    dep_id int AUTO_INCREMENT PRIMARY key,
    dep_name varchar(255)
);



# task based query 

# Part 1: The Environment Setup

# Run this script in your SQL editor to create the sandbox.
 **SQL**

CREATE TABLE Users (
user_id INT PRIMARY KEY,
name VARCHAR(100),
email VARCHAR(100),
signup_date DATE,
country VARCHAR(50)
);
CREATE TABLE Products (
product_id INT PRIMARY KEY,
name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2),
stock_count INT
);
CREATE TABLE Orders (
order_id INT PRIMARY KEY,
user_id INT,
order_date DATE,
status VARCHAR(20),
FOREIGN KEY (user_id) REFERENCES Users(user_id)
);
CREATE TABLE Order_Items (
item_id INT PRIMARY KEY,
order_id INT,
product_id INT,
quantity INT,
unit_price DECIMAL(10,2),
FOREIGN KEY (order_id) REFERENCES Orders(order_id),
FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
Part 2: The 100 Questions (2-Hour Timer)
The Basics (Questions 1–20)
1. Select all columns from the Users table.
2. List the names of all products in the 'Electronics' category.
3. Find all users who signed up in 2023.
4. List products with a price greater than $500.
5. Find all orders with a 'Pending' status.
6. Select the email of the user with user_id 10.
7. List all unique countries in the Users table.
8. Find products where the name starts with 'S'.
9. Get the top 5 most expensive products.
10. Find all orders placed in January 2024.
11. List users whose name contains 'John'.
12. Find products with stock_count between 10 and 50.
13. Get all orders from users in 'USA'.
14. List products sorted by price (lowest to highest).
15. Count the total number of users.
16. Find all products that are NOT in the 'Clothing' category.
17. List orders sorted by order_date descending.
18. Find users who signed up before 2022.
19. Get the names of products that cost exactly $99.99.
20. Show the first 10 rows of the Order_Items table.
**answers**
1. select * from users;
2. select name from products where category = 'Electronics';
3. select * from users where year(signup_date) = 2023;
4. select * from products where price > 500;
5. select * from orders where status = 'Pending';
6. select email from users where user_id = 10;
7. select distinct country from users;
8. select * from products where name like 'S%';
9. select * from products order by price desc limit 0,5;
10. select * from orders where month(order_date) = 1 and year(order_date) = 2024;
11. select * from users where name = 'John';
12. select * from products where stock_count between 10 and 50;
13. select * from users where country = 'USA';
14. select * from products order by price asc;
15. select count(*) from users;
16. select * from products where category != 'Clothing';
17. select * from orders order by order_date desc;
18. select * from users where signup_date < '2022-01-01';
19. select name from products where price = 99.99;
20. select * from order_items limit 0,10;