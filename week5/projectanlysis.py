import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV
df = pd.read_csv("sales.csv")

# Product Sales
sns.barplot(x="Product", y="Sales", data=df)

plt.title("Product Sales Analysis")

plt.show()

# Correlation Heatmap
correlation = df.corr(numeric_only=True)

sns.heatmap(correlation,
            annot=True)

plt.title("Business Correlation")

plt.show()