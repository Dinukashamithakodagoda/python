import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Keyboard", "Mouse"]
sales = [150000, 80000, 25000, 15000]

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()