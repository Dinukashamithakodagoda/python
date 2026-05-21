import pandas as pd

# Read CSV File
df = pd.read_csv("sales.csv")

# Convert Date Column
df["Date"] = pd.to_datetime(df["Date"])

print("\n--- Full Sales Data ---")
print(df)

# Total Sales
print("\nTotal Sales:")
print(df["Sales"].sum())

# Total Profit
print("\nTotal Profit:")
print(df["Profit"].sum())

# Average Sales
print("\nAverage Sales:")
print(df["Sales"].mean())

# Highest Sale
print("\nHighest Sale:")
print(df["Sales"].max())

# Top Selling Product
top_product = df[df["Sales"] == df["Sales"].max()]

print("\nTop Selling Product:")
print(top_product)

# Monthly Sales
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n--- Monthly Sales ---")
print(monthly_sales)

# Monthly Profit
monthly_profit = df.groupby("Month")["Profit"].sum()

print("\n--- Monthly Profit ---")
print(monthly_profit)

# Products Sold More Than 3 Quantity
high_quantity = df[df["Quantity"] > 3]

print("\nProducts Sold More Than 3 Quantity:")
print(high_quantity)

# Total Quantity Sold
print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())