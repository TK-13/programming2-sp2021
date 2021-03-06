"""
Your task is to recreate the plot here: https://drive.google.com/file/d/1YLyShCmcvyBWHNfCzJx7Nz_dFvcAzBCY/view?usp=sharing

Steps:
1. Create a list of the squared x_values
2. Create a list of the cubed x_values
3. Create a green linear line with the label linear
4. Create an orange squared line with the label squares
5. Create a blue cubed line with the label cubes
6. Title the plot Simple Plot
7. Label the x axis Xs
8. Label the y axis Ys
9. Add the legend, and make sure the labels are correct
10. Show the plot!
"""

import matplotlib.pyplot as plt
import numpy as np

# np.linspace() Gives 100 values, equally distributed, between 0 and 2. Range, but with floats.
x_values = np.linspace(0, 2, 100)
y_linear = [x for x in x_values]
y_squares = [x**2 for x in x_values]
y_cubes = [x**3 for x in x_values]

plt.plot(x_values, y_linear, label='Linear', c="green")
plt.plot(x_values, y_squares, label='Squares', c="orange")
plt.plot(x_values, y_cubes, label='Cubes', c="blue")

plt.title('Simple Plot')
plt.xlabel('Xs')
plt.ylabel('Ys')
plt.xticks(rotation=75)  # Tilts x-axis labels.
plt.legend()

plt.show()
