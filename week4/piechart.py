import matplotlib.pyplot as plt

labels = ["Laptop", "Phone", "Keyboard"]
sales = [50, 30, 20]

plt.pie(sales, labels=labels, autopct="%1.1f%%")

plt.title("Sales Distribution")

plt.show()
