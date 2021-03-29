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


# def find_library(library_name, library_data):
#     for library in library_data:
#         if library["LOCATION"] == library_name:
#             return library
#
#
# def plot_library(name):
#     # extract all Harold Washington data
#     library_name = name
#     library = find_library(library_name, library_data)
#     # print(library)
#
#     # filter out data that we actually need
#     visitors = [int(library[month.upper()]) for month in list_of_months]
#     # print(visitors)
#
#     # plot months against number of visitors
#     plt.figure(1, tight_layout=True)
#     plt.plot(list_of_months, visitors, label=library_name)
#
#     # establish plot characteristics in plt.plot
#     plt.xticks(rotation=75)
#     plt.title("Number of Visitors at Libraries in 2019")
#     plt.xlabel("Months")
#     plt.ylabel("Visitors")
#     plt.legend(fancybox=True, shadow=True)
#
#
# for library in library_data:
#     if library["LOCATION"] != "Harold Washtington Library Center":
#         plot_library(library["LOCATION"])
#
# # show the plot
# plt.show()

# libraries = [library_data[i] for i in range(len(library_data))]


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

top_10.reverse()

x_values = [int(item[0]) for item in top_10]
y_values = [item[1] for item in top_10]
print(x_values)
print(y_values)

plt.figure(1, tight_layout=True)
plt.ylabel("Library Name")
plt.xlabel("Visitors YTD")
plt.title("Top 10 Most Popular Libraries")
plt.barh(y_values, x_values)
plt.yticks(rotation=30)

# show the plot
plt.show()

