import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("students.csv")

print(df.head())

# Features
X = df[["StudyHours"]]

# Labels
y = df["Marks"]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

# Predict Marks
prediction = model.predict([[5]])

print("\nPredicted Marks:")
print(prediction)

# Model Details
print("\nCoefficient:")
print(model.coef_)

print("\nIntercept:")
print(model.intercept_)

# Visualization
plt.figure(figsize=(8,5))

plt.scatter(df["StudyHours"],
            df["Marks"])

plt.plot(df["StudyHours"],
         model.predict(X))

plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.title("Student Marks Prediction")

plt.grid(True)

plt.show()