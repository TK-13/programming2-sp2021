import matplotlib.pyplot as plt
import numpy as np

x_values = list(range(50))
squares = [x**2 for x in x_values]

plt.scatter(x_values, squares, s=50)  # change s value for dot size
plt.grid(color='red')
plt.annotate("My Annotation", xy=(49, 49**2))  # xy is x and y coordinates of your annotation

# line of best fit (1st degree -- linear)
p = np.polyfit(x_values, squares, 1)  # (x, y, poly_order)  1st order is linear
print(p)  # return (m, b)
m, b = p

xs_best_fit = x_values
ys_best_fit = [m*x + b for x in xs_best_fit]
plt.plot(xs_best_fit, ys_best_fit)

# line of best fit (2nd degree)
p = np.polyfit(x_values, squares, 2)  # (x, y, poly_order)
print(p)  # return (m, b)
m, b, l = p

xs_best_fit_2 = x_values
ys_best_fit_2 = [m*x**2 + b*x + l for x in xs_best_fit]

plt.plot(xs_best_fit_2, ys_best_fit_2)


plt.show()
