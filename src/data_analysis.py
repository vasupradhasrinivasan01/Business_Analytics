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

# Get Sample Customers Data
customers_sample = run_and_save_query("SELECT * FROM customers LIMIT 10;", "Customers Sample Data","data/generated_output/Customers_Sample_Data.csv")

# Get Customers from Unknown Region
customers_from_unknown = run_and_save_query("SELECT * FROM customers WHERE Region = 'Unknown';", "Customers from Unknown Region", "data/generated_output/Customers_Unknown_Region.csv")

# Get Sample Sales Data
sales_sample = run_and_save_query("SELECT * FROM sales LIMIT 10;", "SELECT * FROM sales LIMIT 10","data/generated_output/Sales_Sample_Data.csv")

# Get Valuable Feedbacks
sales_feedback = run_and_save_query("SELECT * FROM sales WHERE FEEDBACKSCORE = 5;", "Sales Valuable Feedback","data/generated_output/Sales_Feedback_Data.csv")

# Get Zero Quantity Feedbacks
zero_sales = run_and_save_query("SELECT * FROM sales WHERE QUANTITY = 0;", "Zero Quantity Sales","data/generated_output/Zero_Sales.csv")

# Get Nullable Feedbacks
sales_feedback = run_and_save_query("SELECT * FROM sales WHERE FEEDBACKSCORE IS NULL;", "Sales Nullable Feedback","data/generated_output/Sales_Null_Feedback_Data.csv")

# Get Sample Products Data
products_sample = run_and_save_query("SELECT * FROM products LIMIT 10;", "SELECT * FROM products LIMIT 10","data/generated_output/Products_Sample_Data.csv")

# Get Accessories Products
products_sample = run_and_save_query("SELECT * FROM products WHERE CATEGORY = 'Accessories'", "SELECT * FROM products LIMIT 10","data/generated_output/Products_Accessories_Data.csv")
conn.close()

print("✅ CSV files successfully loaded into SQLite database: business_analytics.db")

