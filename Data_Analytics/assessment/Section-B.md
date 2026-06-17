# Section B: Practical Task

1. Execute a query to retrieve the first 20 records from the orders table to verify
data ingestion.

  **answers**
  ```
   select top 20 * from orders;
  ```

2. Select Order ID, Order Date, Sales, and Profit, applying a column alias to
display Sales as Total_Sales.

   **answers**
   ```
    select OrderID, OrderDate, Sales as Total_Sales, Profit from orders;
   ```

3. Filter the dataset to isolate all high-value transactions where the Sales figure
exceeds 5000.

   **answers**
   ```
    select * from orders where Sales > 5000;
   ```


4. Generate a report of the top 10 most profitable orders by sorting the records
by Profit in descending order.

   **answers**
   ```
    select top 10 * from orders order by Profit desc;
   ```
