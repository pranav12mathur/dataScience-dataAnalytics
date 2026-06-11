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
  **answers**
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


 **answers**
1. create table flip_department(
    dep_id int AUTO_INCREMENT PRIMARY key,
    dep_name varchar(255)
);
   create table flip_employee(
    emp_id int AUTO_INCREMENT PRIMARY key,
    emp_name varchar(255),
    age int,
    salary decimal(10,2),
    dep_id int references flip_department(dep_id)
);
2. select ucase(dep_name) from flip_department;
3. select dep_name from flip_department order by dep_name desc;
4. select * from flip_employee where salary < (select max(salary) from flip_employee);
5. select * from flip_employee where emp_id in (3,5,2);
6. select * from flip_employee where emp_name like 'f%';
7. select e.emp_id, e.emp_name, e.age, e.salary, d.dep_name from flip_employee e join flip_department d on e.dep_id = d.dep_id;



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