import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 5, 7, 12, 9]

plt.plot(x, y, marker='o')
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
