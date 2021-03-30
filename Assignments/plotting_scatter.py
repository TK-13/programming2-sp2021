import csv
import matplotlib.pyplot as plt

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

# Make a scatterplot which does the following:
# - Scatter plot the Total Greenhouse gas (GHG) Emissions (y-axis), versus building square footage (x-axis) (10pts)
data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Resources/Chicago_Energy_Benchmarking.csv")
data_reader = csv.DictReader(data_raw)
data = list(data_reader)
data_raw.close()

x_key = "Gross Floor Area - Buildings (sq ft)"
y_key = "Total GHG Emissions (Metric Tons CO2e)"
x = []
y = []

plt.figure(1, tight_layout=True)

# - Data includes ONLY data for K-12 Schools. (4pts)
# - Data includes ONLY data for 2018 reporting. (4pts)
school_data = [row for row in data if
               row["Primary Property Type"] == "K-12 School" and
               row["Data Year"] == "2018"]

# x, y = [ row["x_key"] for row in data if row["Primary Property Type"] == "K-12 School" and row["Data Year"] == "2018", row["y_key"] for row in data if row["Primary Property Type"] == "K-12 School" and row["Data Year"] == "2018"]

# for row in school_data:
#     print(row)

for i in range(len(school_data)):
    x.append(school_data[i][x_key])
    y.append(school_data[i][y_key])

# - Label x and y axis and give appropriate title. (3pts)
# TODO: why is everything so linear, and not spread out?
plt.scatter(x, y, s=1)
plt.xlabel(x_key)
plt.xlabel(y_key)
# plt.axis([0, 800000, 0, 8000])  # [xmin, xmax, ymin, ymax]
plt.title("2018 Greenhouse Gas Emissions for K-12 Chicago Schools")


# - Annotate Francis W. Parker. (5pts) TODO: is this correct? better way to do this, using school data?
plt.annotate("Francis W. Parker", xy=("233000", "2947.9"))

# - Create a best fit line for schools shown. (5pts)

plt.show()
