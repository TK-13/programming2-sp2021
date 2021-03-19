import matplotlib.pyplot as plt

'''
plt.figure(1)  # create a new window/plot

plt.plot([120, 40, 10, 0], label="line 1")  # plot y against the index

#         x                   y
plt.plot([1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36], label="line 2")  # plot x vs y

plt.legend()


plt.figure(2)  # make second window

x1 = [x for x in range(1, 11)]
y1 = [y ** 2 for y in x1]

# plt.plot(x1, y1)

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
plt.plot(x1, y1, color='green', marker='*', markersize=10, linestyle='dashdot', alpha=0.5, label="my first plot")

#  title axes label unit numbers key (TALUNK)
plt.xlabel('time (seconds)')
plt.ylabel('excitement level (YAYS)')
plt.title('Example Plot')
plt.axis([0, 11, 0, 120])  # [xmin, xmax, ymin, ymax]
plt.legend()

plt.show()  # opens the window/plot
'''


xs = [1, 14, 26, 32]
ys = [10, 27, 32, 106]

x1s = [x for x in range(1, 101)]
y1s = [(y**3) for y in x1s]
plt.title('Title')
plt.xlabel('x label')
plt.ylabel('y label')

plt.plot(xs, ys, label='plot 1', marker="o", markeredgecolor='red', lw=10)
plt.plot(x1s, y1s,
         label='plot 2', drawstyle='steps', marker="4", ms=20,
         markeredgecolor='purple', snap=True, lw=5)

plt.show()
