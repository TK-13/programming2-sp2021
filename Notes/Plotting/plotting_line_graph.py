# import plt and csv libraries
import csv
import matplotlib.pyplot as plt

# open the csv file
library_data = open("../../Resources/libraries_visitors_by_location_2019.csv")
library_data = csv.DictReader(library_data)

# read the contents into lists
library_data = list(library_data)

def find_library(library_name, library_data):
    for library in library_data:
        if library["LOCATION"] == library_name:
            return library

# extract all Harold Washington data
library_name = "Harold Washtington Library Center"
library = find_library(library_name, library_data)
print(library)

# filter out data that we actually need
list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
visitors = [int(library[month.upper()]) for month in list_of_months]
print(visitors)

# plot months against number of visitors
plt.figure(1, tight_layout=True) # tight_layout makes everything fit in figure
plt.plot(list_of_months, visitors, color="blue", label=library_name)

# establish plot characteristics in plt.plot
plt.xticks(rotation=75)
plt.title("Number of Visitors at {0} in 2019".format(library_name))
plt.xlabel("Months")
plt.ylabel("Visitors")
plt.legend(fancybox=True, shadow=True)


# show the plot
plt.show()
