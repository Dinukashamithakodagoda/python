import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales.csv")

print(df.head())
print(df.corr(numeric_only=True))