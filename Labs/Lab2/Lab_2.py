import csv
import matplotlib.pyplot as plt
import numpy as np

country_names = []
total_events = []
total_years = [2000, 2010, 2015, 2016]


# This function compiles a chronological list of the total events of the specified country. This is used to efficiently
# populate the event information for each country.
def populate_events(country):
    year_tracker = []
    events = []
    for i in conflict_dataset:
        if i["CountryName"] == country and int(i['Year']) in total_years and i["Year"] not in year_tracker:
            events.append(int(i["TotalEvents"]))
            year_tracker.append(i["Year"])
    return events


# This function returns a chronological list of the suicide rates of the specified country.
def populate_suicides(country):
    suicide_rates = []
    for i in new_suicide_dataset:
        if i["Country"] == country and i["Sex"] == " Both sexes":
            for t in total_years:
                suicide_rates.append(float(i[str(t)]))
    return suicide_rates


# This function just makes it easier to put the datasets into a dictionary.
def read_data(path):
    data_raw = open(path)
    data_reader = csv.DictReader(data_raw)
    file = list(data_reader)
    data_raw.close()
    return file


# Using read_data() to read the respective datasets into dictionaries
new_suicide_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/Age-standardized suicide rates.csv")
conflict_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/gdelt_processor_friendly.csv")
# The 'processor friendly' version only has data beyond the year 2000, since that's roughly the range of the suicide
# data. This way, the program can spend less time looking through all 176k lines of the original dataset, while still
# having to sort through and find the right values, as it normally would.


'''
Example:
my_dict = {
    "USA": {
        "Years": [2018, 2019, ...],
        "Suicide Rates": [1.4, 6.7, ...],
        "Event Numbers": [50, 67, ...]
    },
    "Brazil": {
        "Years": [2018, 2019, ...],
        "Suicide Rates": [1.4, 6.7, ...],
        "Event Numbers": [50, 67, ...]
        }
    }
}

my_dict {
    2018: {
        "USA": {
        "Suicide Rate": 1.4,
        "Num Events": 5
    },
    "Brazil": {
        }
}
'''


# Making Dictionaries for each country
country_dict = {}
for i in new_suicide_dataset:
    if i["Country"] not in country_names:
        country_names.append(i["Country"])
        key = str(i["Country"])
        country_dict[key] = {
            "Years": total_years,
            "Suicide Rates": populate_suicides(key),
            "Events": populate_events(key)
        }

# for k, v in country_dict.items():
#     print(k, "\n", v)

plt.figure(0, tight_layout=True)
target = "China"
x_key = 'Years'
y_key_1 = 'Suicide Rates'
y_key_2 = 'Events'

print(country_dict[target][y_key_1])

x_vals = [x for x in country_dict[target][x_key]]
y1_vals = [y for y in country_dict[target][y_key_1]]
y2_vals = [y for y in country_dict[target][y_key_2]]

plt.plot(x_vals, y1_vals, color="red")
plt.plot(x_vals, y2_vals, color="blue")
plt.title('Simple Plot')
plt.xlabel(x_key)
plt.ylabel("Placeholder")
# plt.xticks(rotation=75, size=5)
# plt.yticks(size=5)

plt.show()
