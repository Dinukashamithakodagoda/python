import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales.csv")

print(df.head())

sns.lineplot(x="Date", y="Sales", data=df)

plt.title("Sales Trend")

plt.xticks(rotation=45)

plt.show()