import sqlite3
import pandas as pd
import os

# Path to your generated CSV files
products_csv = r"/home/runner/work/Business_Analytics/Business_Analytics/data/generated_output/products_data.csv"
customers_csv = r"/home/runner/work/Business_Analytics/Business_Analytics/data/generated_output/customers_data.csv"
sales_csv = r"/home/runner/work/Business_Analytics/Business_Analytics/data/generated_output/sales_data.csv"

# Load CSVs into DataFrames
products_df = pd.read_csv(products_csv)
customers_df = pd.read_csv(customers_csv)
sales_df = pd.read_csv(sales_csv)

# Create SQLite connection (this will create a file-based database)
conn = sqlite3.connect("business_analytics.db")

# Write DataFrames to SQLite tables
products_df.to_sql("products", conn, if_exists="replace", index=False)
customers_df.to_sql("customers", conn, if_exists="replace", index=False)
sales_df.to_sql("sales", conn, if_exists="replace", index=False)

conn.commit()

def run_and_save_query(query, question, filename):
    df = pd.read_sql(query, conn)
    df['__Question__'] = question
    df['__Query__'] = query  # Add query text as a column (same for all rows)
    df.to_csv(filename, index=False)
    print(f"✅ Query result saved to {filename}")
    return df

# Example 1: Get first 10 customers
customers_sample = run_and_save_query("SELECT * FROM customers LIMIT 10;", "SELECT * FROM customers LIMIT 10","data/generated_output/Customers_Query_Results.csv")

sales_sample = run_and_save_query("SELECT * FROM sales LIMIT 10;", "SELECT * FROM sales LIMIT 10","data/generated_output/Sales_Query_Results.csv")

products_sample = run_and_save_query("SELECT * FROM products LIMIT 10;", "SELECT * FROM products LIMIT 10","data/generated_output/Products_Query_Results.csv")

conn.close()

print("✅ CSV files successfully loaded into SQLite database: business_analytics.db")

