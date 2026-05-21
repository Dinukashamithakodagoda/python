import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("sales.csv")

# Monthly Sales
monthly_sales = df.groupby("Date")["Sales"].sum()

# Plot
plt.plot(monthly_sales)

plt.title("Sales Report")
plt.xlabel("Date")
plt.ylabel("Sales")

plt.show()