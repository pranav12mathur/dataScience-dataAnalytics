# SQL practice tables:
 
 **customer table**
  
  1. create:
  
   ```
    create table customer(
    customer_id int AUTO_INCREMENT primary key,
    customer_name varchar(100),
    email varchar(100),
    phone bigint,
    address varchar(100),
    city varchar(100),
    join_date date,
    is_active boolean
);
   ```
  
  2. alter:
  
    ```
    ALTER table customer add age int after customer_name
    alter table customer drop city
    alter table customer change customer_name name varchar(100)
    ```
  
  3. rename:
  
    ```
    alter table customer rename to customers
  
    ```
  
  4. drop:
  
    ```
    drop table customers
    ```
  
  5. truncate:
    
    ```
    truncate table customers
    ```  
  
  
 **cart table**
  
  1. create:
   
   ```
    create table cart(
    cart_id int AUTO_INCREMENT primary key,
    customer_id int,
    product_id int,
    quantity int,
    total_price decimal(10,2),
    added_date varchar(100),
    start_date date,
    status varchar(100),
    discount_amount decimal(10,2)
);
   ```
  
  2. alter:
    
    ```
    ALTER table cart add expiry_date date after start_date
    alter table cart drop status
    alter table cart change added_date added_time varchar(100)
    ```
  
  3. rename:
    
    ```
    alter table cart rename to flip_cart
    ```
  
  4. drop:
    
    ```
    drop table cart
    ```
  5. truncate: 
    
    ```
    truncate table cart
    ```
 
 **payment table**
  
  1. create:
   
   ```
    create table payment(
    payment_id int AUTO_INCREMENT primary key,
    order_id int,
    payment_method varchar(100),
    amount decimal(10,2),
    payment_date date,
    transaction_id varchar(100),
    payment_status varchar(100),
    currency char(5)
);
   ```
  
  2. alter:
    
    ```
    ALTER table payment add refund_date date after payment_date
    alter table payment drop currency
    alter table payment change payment_method method varchar(100)
    ```
  
  3. rename:
   
    ```
    alter table payment rename to flip_payment
    ```
  
  4. drop:
    
    ```
    drop table payment
    ```
  
  5. truncate: 
    
    ```
    truncate table payment
    ```

  
  **seller table**
  
  1. create:
   
   ```
    create table seller(
    seller_id int AUTO_INCREMENT PRIMARY key,
    seller_name varchar(100),
    email varchar(100),
    phone bigint,
    buisness_name varchar(100),
    address varchar(100),
    rating decimal(1,1),
    join_date date
);
   ```
  
  2. alter:
    
    ```
    ALTER table seller add tax_id varchar(100)
    alter table seller drop buisness_name
    alter table seller change seller_name name varchar(100)
    ```
  
  3. rename:
    
    ```
    alter table seller rename to flip_seller
    ```
  
  4. drop:
    
    ```
    drop table seller
    ```
  
  5. truncate: 
    
    ```
    truncate table seller
    ``` 
 
 
 **delivery table**
  
  1. create:
   
   ```
    create table delivery(
    delivery_id int AUTO_INCREMENT primary key,
    order_id int,
    delivery_partner varchar(100),
    tracking_number int,
    dispatch_date date,
    delivery_date date,
    delivery_status varchar(100),
    delivery_charge decimal(10,2)
);
   ```
  
  2. alter:
    
    ```
    alter table delivery add estimated_delivery_date date
    alter table delivery drop delivery_charge
    alter table delivery change delivery_partner partner_name varchar(100)
    ```
  
  3. rename:
    
    ```
    alter table delivery rename to flip_delivery
    ```
  
  4. drop:
    
    ```
    drop table delivery
    ```
  
  5. truncate: 
    
    ```
    truncate table delivery
    ```         
 
 **wishlist table**
  
  1. create:
   
   ```
    create table wishlit(
    wishlit int AUTO_INCREMENT PRIMARY key,
    customer_id int,
    product_id int,
    added_date date,
    priority_level varchar(100),
    price_alert boolean DEFAULT true,
    stock_alert boolean DEFAULT true,
    wishlit_status varchar(100)
);
   ```
  
  2. alter:
    
    ```
    alter table wishlit add expiry_date date
    alter table wishlit drop stock_alert
    alter table wishlit change wishlit_status status varchar(100)
    ```
  
  3. rename:
    
    ```
    alter table wishlit rename to flip_wishlit
    ```
  
  4. drop:
    
    ```
    drop table wishlit
    ```
  
  5. truncate: 
    
    ```
    truncate table wishlit
    ```            

 
 **category table**
  
  1. create:
   
   ```
    create table category(
    category_id int AUTO_INCREMENT PRIMARY key,
    category_name varchar(100),
    category_image blob,
    parent_category varchar(100),
    description text,
    total_products int,
    created_date date,
    category_status varchar(100)
);
   ```
  
  2. alter:
    
    ```
    alter table category add updated_date date
    alter table category drop total_products
    alter table category change category_name name varchar(100)
    ```
  
  3. rename:
    
    ```
    alter table category rename to flip_category
    ```
  
  4. drop:
    
    ```
    drop table category
    ```
  
  5. truncate: 
    
    ```
    truncate table category
    ```               