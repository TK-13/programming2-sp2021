'''
CTA Ridership (22pts)
Get the csv from the following data set.
https://data.cityofchicago.org/api/views/w8km-9pzd/rows.csv?accessType=DOWNLOAD
This shows CTA ridership by year going back to the 80s
It has been updated with 2018 data, but not yet with anything after unfortunately
'''

import csv
import matplotlib.pyplot as plt


# 1  Download the dataset and read in the file.
cta_data_open = open("/Users/tkmuro/PycharmProjects/tkProgramming/Assignments/CTA_-_Ridership_-_Annual_Boarding_Totals.csv")
cta_data = csv.DictReader(cta_data_open)
cta_data = list(cta_data)
cta_data_open.close()


# 2  Retrieve the bus, rail, and total data for the last 15 years from the csv file. (5pts)
years = []
bus_data = []
rail_data = []
paratransit_data = []
total_data = []
all_y_list = [years, bus_data, paratransit_data, rail_data, total_data]


def populate(parameter):
    target_list = [int(cta_data[i][parameter]) for i in range(len(cta_data))]
    return target_list


years = populate("year")
bus_data = populate("bus")
rail_data = populate("rail")
paratransit_data = populate("paratransit")
total_data = populate("total")
all_y_list = [bus_data, paratransit_data, rail_data, total_data]


# 3  Make a line plot of rail usage for the last 15 years of data.  (year on x axis, and ridership on y) (3pts)
def plot_in_range(data_list, start, label_name):
    plt.plot([year for year in years[start:]], [d for d in data_list[start:]], label=label_name)


plot_in_range(rail_data, 15, "Rails")


# 4  Plot bus usage for the same years as a second line on your graph. (3pts)
plot_in_range(bus_data, 15, "Buses")


# 5  Plot total usage on a third line on your graph. (3pts)
plot_in_range(total_data, 15, "Total")


# 6  Add a title and label your axes. (3pts)
plt.title('CTA usage from 2003 to 2018:')
plt.xlabel('Years')
plt.ylabel('Usage')


# 7  Add a legend to show data represented by each of the three lines. (3pts)
plt.legend()

plt.show()


# 8  What trend or trends do you see in the data?  Offer a hypotheses which might explain the trend(s). Just add a comment here to explain. (2pts)
'''
The use of rail transportation increases steadily from 2003 to 2018, while the use of buses declines after it's 
peak in 2008. However, buses were consistently been used more than rails throughout all 15 years. The total use of 
CTA peaks at around 2012, before declining to 2003-like levels. One possible explanation for these trends is an 
increase in individually-owned cars over time (which I'm assuming has occurred). As more people own cars, there is 
less demand for public transportation. More cars also means more traffic, which slows down buses and consequently makes 
rails a faster option for public transportation. Thus, the overall use of CTA decreases, buses become less popular, and
rails become more popular. While this hypothesis would fit the trends shown in the data, I have absolutely no idea
whether car ownership has increased since 2004. 
'''
