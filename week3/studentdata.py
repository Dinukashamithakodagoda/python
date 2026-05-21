import pandas as pd

data = {
    "Name": ["Kamal", "Nimal", "Sunil", "Kasun"],
    "Marks": [80, 75, 90, 60]
}

df = pd.DataFrame(data)

print("\n--- Student Data ---")
print(df)

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nStudents Above 70:")
print(df[df["Marks"] > 70])