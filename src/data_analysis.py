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

OUTPUT_DIR = "generated_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Function to run query and save result along with query text
def run_and_save_query(query, question, filename):
    df = pd.read_sql(query, conn)
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(f"# Query: {query}\n")
        df.to_csv(f, index=False)
    print(f"✅ Query result saved to {filename}")
    return df

# Example 1: Get first 10 customers
customers_sample = run_and_save_query("SELECT * FROM customers LIMIT 10;", "SELECT * FROM customers LIMIT 10","Customers_Query_Results.csv")

sales_sample = run_and_save_query("SELECT * FROM sales LIMIT 10;", "SELECT * FROM sales LIMIT 10","Sales_Query_Results.csv")

products_sample = run_and_save_query("SELECT * FROM products LIMIT 10;", "SELECT * FROM products LIMIT 10","Products_Query_Results.csv")

conn.close()

print("✅ CSV files successfully loaded into SQLite database: business_analytics.db")

