import sqlite3
import pandas as pd

# Connect to your SQLite database
conn = sqlite3.connect("business_analytics.db")

# Example 1: Get first 10 customers
query = "SELECT * FROM customers LIMIT 10;"
customers_sample = pd.read_sql(query, conn)
print(customers_sample)

# Example 2: Get all sales for a specific CustomerID
customer_id = 1234
query = f"SELECT * FROM sales WHERE CustomerID = {customer_id};"
sales_for_customer = pd.read_sql(query, conn)
print(sales_for_customer)

# Example 3: Get products with Price > 1000
query = "SELECT ProductName, Price FROM products WHERE Price > 1000;"
expensive_products = pd.read_sql(query, conn)
print(expensive_products)

conn.close()
