# Section A: Concept Application

1. What is the functional difference between SELECT * and specifying column
names, and when is each preferred?

   **answers**
   ```
    Functionally, `SELECT *` retrieves all columns from a table, while specifying column names allows you to retrieve only the columns you need. Using `SELECT *` can lead to unnecessary data retrieval and increased resource usage, especially if the table has many columns or large data types. Specifying column names is preferred when you want to optimize performance and reduce the amount of data transferred, particularly in production environments or when working with large datasets.
   ```

2. Which keyword renames a column in the output, and does this alias change
the actual table structure in the database?

   **answers**
   ```
    The keyword used to rename a column in the output is `AS`. This alias does not change the actual table structure in the database; it only affects the display of the results in the query output. The underlying table remains unchanged, and the alias is only temporary for that specific query execution.
   ```

3. Why does wrapping a numeric value in quotes (e.g., '5000') in a WHERE clause
create a data type conflict in SQL?

    **answers**
    ```
     Wrapping a numeric value in quotes (e.g., '5000') treats it as a string rather than a numeric type. When the database engine attempts to compare this string to a numeric column in the WHERE clause, it can lead to a data type conflict because the types do not match. This can result in errors or unexpected behavior, as the database may not be able to implicitly convert the string to a number for comparison.
    ```

4. Contrast the results of ORDER BY Profit DESC versus ASC when the goal is to
identify the top 10 most profitable orders.

    **answers**
    ```
     Using `ORDER BY Profit DESC` will sort the results in descending order, meaning the highest profit values will appear first. This is ideal for identifying the top 10 most profitable orders, as you can simply take the first 10 rows of the sorted result set. Conversely, `ORDER BY Profit ASC` sorts the results in ascending order, placing the lowest profit values at the top. If you were to use this sorting method, you would need to look at the last 10 rows to find the most profitable orders, which is less efficient and counterintuitive for this specific goal.
    ```

5. What is the T-SQL equivalent of the LIMIT clause in MS SQL Server, and why
does syntax vary across SQL engines?

  
   **answers**
   ```
    The T-SQL equivalent of the LIMIT clause in MS SQL Server is the `TOP` clause. For example, to retrieve the top 10 rows, you would use `SELECT TOP 10 * FROM TableName`. Syntax varies across SQL engines because each database management system (DBMS) has its own implementation and extensions of the SQL standard. These variations can be due to historical reasons, performance optimizations, or additional features provided by the specific DBMS.
   ```

6. Explain the logical execution order of a query containing SELECT, WHERE, ORDER
BY, and LIMIT clauses.

  
   **answers**
   ```
    The logical execution order of a query containing SELECT, WHERE, ORDER BY, and LIMIT clauses is as follows:
    1. FROM: The database engine first identifies the source tables and joins them if necessary.
    2. WHERE: Next, it filters the rows based on the conditions specified in the WHERE clause.
    3. SELECT: After filtering, the engine selects the specified columns from the remaining rows.
    4. ORDER BY: The results are then sorted according to the criteria defined in the ORDER BY clause.
    5. LIMIT (or TOP): Finally, the engine applies the LIMIT or TOP clause to return only the specified number of rows from the sorted result set.

    This logical order ensures that filtering and sorting are applied before limiting the number of results returned.
   ```
