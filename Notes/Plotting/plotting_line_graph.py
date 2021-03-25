# import plt and csv libraries
import csv
import matplotlib.pyplot as plt

# open the csv file
library_data = open("../../Resources/libraries_visitors_by_location_2019.csv")
library_data = csv.DictReader(library_data)
list_of_months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

# read the contents into lists
library_data = list(library_data)


# Bar Graphs

library_data = list(library_data)
libraries = [library_data[i] for i in range(len(library_data))]
print(libraries)


def get_visitors(lib):
    x = lib["LOCATION"]
    y = lib["YTD"]
    return int(y), x


values = []

for library in libraries:
    values.append(get_visitors(library))

print()
for i in range(len(values)):
    print(values[i])

sorted_values = sorted(values, reverse=True)
top_10 = sorted_values[0:10]
print(top_10)
print()
for i in range(len(top_10)):
    print(top_10[i])

x_values = [int(item[0]) for item in top_10]
y_values = [item[1] for item in top_10]
# y_new = y_values.
print(x_values)
print(y_values)
# print(y_new)

plt.figure(1, tight_layout=True)
plt.barh(y_values, x_values)
plt.yticks(rotation=30)

# show the plot
plt.show()

