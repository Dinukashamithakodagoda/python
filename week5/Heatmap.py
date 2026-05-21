import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales.csv")

print(df.head())



correlation = df.corr(numeric_only=True)

sns.heatmap(correlation,
            annot=True)

plt.title("Correlation Heatmap")

plt.show()