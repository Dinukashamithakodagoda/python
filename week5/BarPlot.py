import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales.csv")

print(df.head())

sns.barplot(x="Product", y="Sales", data=df)

plt.title("Product Sales")

plt.show()