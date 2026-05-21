import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
df = pd.read_csv("sales.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"])

# Extract Month
df["Month"] = df["Date"].dt.month

# -----------------------------
# Dashboard Summary
# -----------------------------

print("\n--- SALES DASHBOARD ---")

# Total Sales
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)

# Total Profit
total_profit = df["Profit"].sum()
print("Total Profit:", total_profit)

# Average Sales
average_sales = df["Sales"].mean()
print("Average Sales:", average_sales)

# Top Product
top_product = df.groupby("Product")["Sales"].sum().idxmax()

print("Top Product:", top_product)

# -----------------------------
# Monthly Sales Chart
# -----------------------------

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.plot(monthly_sales.index,
         monthly_sales.values,
         marker='o')

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(True)

plt.show()

# -----------------------------
# Product Sales Bar Chart
# -----------------------------

product_sales = df.groupby("Product")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.bar(product_sales.index,
        product_sales.values)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

# -----------------------------
# Sales Distribution Pie Chart
# -----------------------------

plt.figure(figsize=(7,7))

plt.pie(product_sales.values,
        labels=product_sales.index,
        autopct="%1.1f%%")

plt.title("Sales Distribution")

plt.show()