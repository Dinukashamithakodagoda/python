import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")

print(df.head())
X = df[["Advertising"]]

y = df["Sales"]

model = LinearRegression()
model.fit(X, y)
prediction = model.predict([[8000]])

print("Predicted Sales:", prediction)
print(model.coef_)
print(model.intercept_)

plt.scatter(df["Advertising"], df["Sales"])

plt.plot(df["Advertising"],
         model.predict(X))

plt.xlabel("Advertising")
plt.ylabel("Sales")

plt.title("Sales Prediction Model")

plt.show()