import csv
import matplotlib.pyplot as plt
import numpy as np

# open csv file and reading through it
data = open("../../Resources/insurance.csv")
data = csv.DictReader(data)

# separate the csv values into more usable lists
data = list(data)
x, y = [int(person['age']) for person in data], [float(person['charges']) for person in data]

# plot it as a scatter plot
plt.scatter(x, y, s=10)

# find and plot the line of best fit
p = np.polyfit(x, y, 1)
print(p)  # return (m, b)
m, b = p

xs_best_fit = [i for i in range(max(x) + 5)]
ys_best_fit = [m*x + b for x in xs_best_fit]
plt.plot(xs_best_fit, ys_best_fit)

plt.xlabel("Age")
plt.ylabel("Health Insurance Charges")
plt.title("Age vs. Health Insurance Charges")

# show it
plt.show()

"""
Your challenges:
1. Maintain the same plot above, but have the dots be one color for smoker, and another color for non smoker.
2. Find and plot the lines of best fit for smokers and non smokers
3. Plot a point for you on the graph and label it with your name. You can make up your health charges.
3. Make another plot, this time bmi vs. charges
4. Color the dots one color for male, and one color for female
5. Find the lines of best fit for male and female
6. Find the point of intersection for the lines, and plot and label it.
"""