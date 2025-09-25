import sqlite3
import pandas as pd

# Path to your generated CSV files
products_csv = r"/home/runner/work/Business_Analytics/Business_Analytics/data/generated_output/products_data.csv"
customers_csv = r"/home/runner/work/Business_Analytics/Business_Analytics/data/generated_output/customers_clean_data.csv"
sales_csv = r"/home/runner/work/Business_Analytics/Business_Analytics/data/generated_output/sales_clean_data.csv"

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
conn.close()

print("✅ CSV files successfully loaded into SQLite database: business_analytics.db")
