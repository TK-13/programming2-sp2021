import csv
import matplotlib.pyplot as plt

library_data = open("../../Resources/libraries_visitors_by_location_2019.csv")
reader = csv.reader(library_data)  # makes a reader object
data = list(reader)

# plot the attendance data for our favorite library

header = data.pop(0)
print(data)
print(header)

# plot top 10 libraries for YTD totals
plt.figure(1, tight_layout=True, figsize=(14, 6))  # figsize in inches

data.sort(key=lambda x: int(x[-1]))
print(data)

top_ten = data[-10:]
top_ten_ytd = [int(x[-1]) for x in top_ten]

top_ten_names = [x[0] for x in top_ten]
x_vals = [x for x in range(len(top_ten))]

plt.barh(x_vals, top_ten_ytd)  # barh is a horizontal bar graph
plt.yticks(x_vals, top_ten_names, fontsize=10)

plt.xlabel("Visitors YTD")
plt.title("Top Ten Most Visited Chicago Libraries")

plt.show()

