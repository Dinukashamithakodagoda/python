import pandas as pd

data = {
    "Name": ["Kamal", "Nimal", "Sunil"],
    "Marks": [80, 75, 90]
}

df = pd.DataFrame(data)

print(df)

print(df.head())

print(df.describe())
print(df.info())
print(df.describe())
print(df["Marks"])
print(df["Marks"].mean())
print(df["Marks"].max())
print(df["Marks"].min())

high_marks = df[df["Marks"] > 80]

print(high_marks)