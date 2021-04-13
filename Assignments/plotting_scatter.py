import csv
import matplotlib.pyplot as plt
import numpy as np

"""
Greenhouse gas emissions (GHG) vs. square footage for all school buildings in Chicago

Data set used will be Chicago Energy Benchmark info from 2018
data can be found at...
https://data.cityofchicago.org/api/views/xq83-jr8c/rows.csv?accessType=DOWNLOAD

Energy Efficiency of Chicago Schools (31pts)

Chicago requires that all buildings over 50000 square feet in the city comply with energy benchmark reporting each year.
The dataset at the link above is that data from 2015 to 2018.
We will use this data to look at schools.  We will visualize the efficiency of schools by scatter plot.
We expect that the more square footage (sqft) a school is, the more greenhouse gas (ghg) emission it will produce.
It would also be interesting to know where Parker lies on this graph???  Let's find out.



Extra Credit: Add a significant feature to your graph that helps tell the story of your data.
(feel free to use methods from matplotlib.org). (5pts)

Note: With extra credit you will earn you a max of 31pts (100%) for the assignment.
Maybe you can try one of the following or think up your own:
- Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
- Make schools in top 10 percent of GHG Intensity show in green.
- Make schools in bottom 10 percent GHG Intesity show in red.
- Add colleges and universities (use a different marker type)
"""

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Resources/Chicago_Energy_Benchmarking.csv")
data_reader = csv.DictReader(data_raw)
data = list(data_reader)
data_raw.close()

x_key = "Gross Floor Area - Buildings (sq ft)"
y_key = "Total GHG Emissions (Metric Tons CO2e)"
x = []
y = []
x_u = []
y_u = []


# Req 6. Create a best fit line for schools shown. (5pts)
def best_fit(x_in, y_in):
    p = np.polyfit(x_in, y_in, 1)
    m, b = p
    xs_best_fit = [i for i in range(int(max(x_in)))]
    ys_best_fit = [m * x + b for x in xs_best_fit]
    plt.plot(xs_best_fit, ys_best_fit, color='black')


# Req 1. Scatter plot the Total Greenhouse gas (GHG) Emissions (y-axis), versus building square footage (x-axis) (10pts)
def scatter(input_data, marker, color, title):
    for i in range(len(input_data)):
        x.append(float(input_data[i][x_key]))
        y.append(float(input_data[i][y_key]))

    # Req 4. Label x and y axis and give appropriate title. (3pts)
    plt.scatter(x, y, s=1, marker=marker, color=color)
    plt.xlabel(x_key)
    plt.ylabel(y_key)
    plt.title(title)

    best_fit(x, y)


# Req 2. Data includes ONLY data for K-12 Schools. (4pts)
# Req 3. Data includes ONLY data for 2018 reporting. (4pts)
def filtered_data(property):
    new_list = [row for row in data if
               row["Primary Property Type"] == property and
               row["Data Year"] == "2018" and
               row[y_key] != '' and row[x_key] != '']
    return new_list


plt.figure(1)
school_data = filtered_data("K-12 School")
scatter(school_data, 'o', 'blue', "2018 Greenhouse Gas Emissions for K-12 Chicago Schools")

# Req 5. Annotate Francis W. Parker. (5pts)
plt.annotate("Francis W. Parker", xy=(233000, 2947.9))

# EC. Annotated labels (school name) for the 3 highest and 3 lowest GHG Intensities.
ymax = 0
ymin = 1000000
max_list = []
min_list = []
for school in school_data:
    if float(school[y_key]) > float(ymax):
        ymax = school[y_key]
        max_list.append(school)
    elif float(school[y_key]) < float(ymin):
        ymin = school[y_key]
        min_list.append(school)

max_list = max_list[-3:]
min_list = min_list[-3:]

for item in max_list:
    plt.annotate("High: " + item["Property Name"], xy=(float(item[x_key]), float(item[y_key])))
for item in min_list:
    plt.annotate("Low: " + item["Property Name"], xy=(float(item[x_key]), float(item[y_key])))


# Add colleges and universities (use a different marker type)
# Note: I made a new figure for College/University data, because having them both on the same graph made the school
# data hard to read.
plt.figure(2)
univ_data = filtered_data("College/University")
scatter(univ_data, "*", 'green', "2018 Greenhouse Gas Emissions for Colleges and Universities")

plt.show()
