import csv
import matplotlib.pyplot as plt
import numpy as np

# open csv file and reading through it
data_raw = open("../../Resources/insurance.csv")
data_reader = csv.DictReader(data_raw)
# separate the csv values into more usable lists
data = list(data_reader)
data_raw.close()


def scatter(x_param, y_param, x_filter, filter_desired_out, color_1, color_2):
    # could have used comprehension. This is actually more efficient, because comprehension would have required 4
    # loops through data. For larger datasets, this would be way more efficient.
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []
    for person in data:
        if person[x_filter] == filter_desired_out:
            x_1.append(float(person[x_param]))
            y_1.append(float(person[y_param]))
        elif person[x_filter] != filter_desired_out:
            x_2.append(float(person[x_param]))
            y_2.append(float(person[y_param]))

    # plot it as a scatter plot
    plt.scatter(x_1, y_1, s=10, color=color_1)
    plt.scatter(x_2, y_2, s=10, color=color_2)
    return x_1, x_2, y_1, y_2


def best_fit_line(x1, x2, y1, y2, color_1, color_2, xlabel, ylabel, title, findintersect=False):
    x_1 = [int(i) for i in x1]
    x_2 = [int(i) for i in x2]

    # find and plot the line of best fit
    best_line_1 = np.polyfit(x_1, y1, 1)
    best_line_2 = np.polyfit(x_2, y2, 1)
    m_1, b_1 = best_line_1
    m_2, b_2 = best_line_2

    x1_best_fit = [i for i in range(max(x_1) + 5)]
    x2_best_fit = [i for i in range(max(x_2) + 5)]
    y1_best_fit = [m_1 * x_1 + b_1 for x_1 in x1_best_fit]
    y2_best_fit = [m_2 * x_2 + b_2 for x_2 in x2_best_fit]

    # xy1 = [[x1_best_fit[i], y1_best_fit[i]] for i in range(len(y1_best_fit))]
    # xy2 = [[x2_best_fit[i], y2_best_fit[i]] for i in range(len(y2_best_fit))]
    # for j in range(len(xy1)):
    #     if xy1[j] in xy2:
    #         plt.scatter(j, x1_best_fit[j], s=30, color='red')
    #         print("found")

    # for r in range(len(y1_best_fit)):
    #     if x1_best_fit[r] == x2_best_fit[r] and y1_best_fit[r] == y2_best_fit[r]:
    #         plt.scatter(r, x1_best_fit[r], s=30, color='red')
    #         print("found")

    if findintersect:
        xi = (b_1 - b_2) / (m_2 - m_1)
        yi = m_1 * xi + b_1

        print('(xi,yi)', xi, yi)
        plt.scatter(xi, yi, color='black')
        # I had to look up how to find the intersect. Commented above, you can see my previous attempts.
        # https://moonbooks.org/Articles/How-to-write-a-simple-python-code-to-find-the-intersection-point-between-two-straight-lines-/

    plt.plot(x1_best_fit, y1_best_fit, color=color_1)
    plt.plot(x2_best_fit, y2_best_fit, color=color_2)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)


plt.figure(1)
scatter('age', 'charges', 'smoker', 'yes', 'black', 'blue')
plt.scatter(5, 9.4*(10**3), s=10, color='green')
plt.annotate("Ryan and TK", xy=(5, 9.4*(10**3)))


plt.figure(2)
scatter('bmi', 'charges', 'sex', 'female', 'orange', 'blue')


# show it
plt.show()

"""
Your challenges:
1. Maintain the same plot above, but have the dots be one color for smoker, and another color for non smoker.       √
2. Find and plot the lines of best fit for smokers and non smokers                                                  √
3. Plot a point for you on the graph and label it with your name. You can make up your health charges.              √
3. Make another plot, this time bmi vs. charges                                                                     √
4. Color the dots one color for male, and one color for female                                                      √
5. Find the lines of best fit for male and female                                                                   √
6. Find the point of intersection for the lines, and plot and label it.
"""