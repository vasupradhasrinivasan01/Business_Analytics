import pandas as pd
import os

df1 = pd.read_csv(r"data/raw_Data/customers_raw_data.csv")

df1.notnull()
df1.dropna()

# print(df1.columns)

df1['Email'] = df1['Email'].str.replace(r'@.*','@email.com',regex=True)
df1['Region'] = df1['Region'].fillna('Unknown')
df1=df1.dropna(subset='Name')
df1=df1.dropna(subset='Email')
df1=df1[~df1['Name'].str.contains(r'Jr.|Sr.', case=False,na=False)]
# print(df1)

# Considering sales dataframe
df2 = pd.read_csv(r"data/raw_Data/sales_raw_data.csv")

df2.notnull()
df2.dropna()

# print(df2.columns)

df2 = df2.dropna(subset='CustomerID')
df2['FeedbackScore'] = df2['FeedbackScore'].fillna('NULL')
df2['Quantity'] = df2['Quantity'].abs()
df2['Quantity'] = df2['Quantity'].fillna(0.0)
df2['SaleDate'] = pd.to_datetime(df2['SaleDate'])
df2['Only_Date'] = df2['SaleDate'].dt.year.astype(str) + "-" + df2['SaleDate'].dt.month.astype(str) + "-" + df2['SaleDate'].dt.day.astype(str)
df2['Only_Time'] = df2['SaleDate'].dt.time
# print(df2)


df3 = pd.read_csv(r"data/raw_Data/products_raw_data.csv")

df3.notnull()
df3.dropna()

# print(df3.columns)
df3 = df3.dropna(subset='ProductName')
df3 = df3[~df3['ProductName'].str.contains(r'Plus | Pro' ,case=False,na=False)]
df3=df3.dropna(subset='Price')
df3['Category'] = df3['Category'].fillna('Accessories')

rint("🔎 Current working directory:", os.getcwd())  # see where script is running
os.makedirs("data/generated_output", exist_ok=True)  # create folder if missing

output_path = "data/generated_output/products_data.csv"
df1.to_csv(output_path, index=False)

print(f"✅ File saved at: {os.path.abspath(output_path)}")
print("📂 Files in output folder:", os.listdir("data/generated_output"))

# os.makedirs("data/generated_output", exist_ok=True)
# df1.to_csv("data/generated_output/products_data.csv", index=False)
# df2.to_csv("data/generated_output/customers_clean_data.csv")
# df3.to_csv("data/generated_output/sales_clean_data.csv")