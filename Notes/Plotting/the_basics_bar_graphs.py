import matplotlib.pyplot as plt
import random

numbers = [random.randint(1, 10) for i in range(5000)]

x_vals = [i for i in range(1, 11)]
y_vals = [numbers.count(y) for y in range(1, 11)]

plt.figure(1)

plt.bar(x_vals, y_vals, label="Favorite Number")
plt.xticks(x_vals)
plt.xlabel("Favorite Number")
plt.ylabel("Number of People")
plt.title("Number of People and their Favorite Numbers")

plt.legend()
plt.show()

plt.figure(2)

plt.barh(x_vals, y_vals, label="Favorite Numbers")  # plot the data in a horizontal bar graphs
plt.yticks(x_vals)

plt.xlabel("Number of People")
plt.ylabel("Favorite Number")
plt.title("Number of People and their Favorite Numbers")
plt.legend()
plt.show()

