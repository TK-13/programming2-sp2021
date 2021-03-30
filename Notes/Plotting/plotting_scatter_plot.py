import csv
import matplotlib.pyplot as plt
import numpy as np

# open csv file and reading through it
data = open("../../Resources/insurance.csv")
data_reader = csv.DictReader(data)
data.close()

# separate the csv values into more usable lists
data = list(data_reader)
# x = [int(person['age']) for person in data]
# y_smoker = [float(person['charges']) for person in data if person['smoker'] == 'yes']
# y_nonsmoker = [float(person['charges']) for person in data if person['smoker'] == 'no']

x_s = []
y_s = []
x_n = []
y_n = []
# could have used comprehension. This is actually more efficient, because comprehension would have required 4
# loops through data. For larger datasets, this would be way more efficient.
for person in data:
    if person['smoker'] == 'yes':
        x_s.append(int(person['age']))
        y_s.append(float(person['charges']))
    elif person['smoker'] == 'no':
        x_n.append(int(person['age']))
        y_n.append(float(person['charges']))

# plot it as a scatter plot
plt.scatter(x_s, y_s, s=10, color='black')
plt.scatter(x_n, y_n, s=10, color='blue')
plt.scatter(5, 9.4*(10**3), s=10, color='green')

print(x_s)
print()
print(x_n)

x_s = [int(i) for i in x_s]
x_n = [int(i) for i in x_n]

print(x_s)
print()
print(x_n)

# find and plot the line of best fit
p_smoker = np.polyfit(x_s, y_s, 1)
p_nonsmoker = np.polyfit(x_n, y_n, 1)
print(p_smoker)  # return (m, b)
print(p_nonsmoker)  # return (m, b)
m_s, b_s = p_smoker
m_n, b_n = p_nonsmoker

xs_best_fit = [i for i in range(max(x_s) + 5)]
xs_best_fit = [i for i in range(max(x_n) + 5)]
ys_best_fit_smoker = [m_s*x_s + b_s for x_s in xs_best_fit]
ys_best_fit_non = [m_n*x_n + b_n for x_n in xs_best_fit]
plt.plot(xs_best_fit, ys_best_fit_smoker, color='black')
plt.plot(xs_best_fit, ys_best_fit_non, color='blue')
plt.annotate("Ryan and TK", xy=(5, 9.4*(10**3)))

plt.xlabel("Age")
plt.ylabel("Health Insurance Charges")
plt.title("Age vs. Health Insurance Charges")

# show it
plt.show()

"""
Your challenges:
1. Maintain the same plot above, but have the dots be one color for smoker, and another color for non smoker.       √
2. Find and plot the lines of best fit for smokers and non smokers                                                  √
3. Plot a point for you on the graph and label it with your name. You can make up your health charges.              √
3. Make another plot, this time bmi vs. charges
4. Color the dots one color for male, and one color for female
5. Find the lines of best fit for male and female
6. Find the point of intersection for the lines, and plot and label it.
"""