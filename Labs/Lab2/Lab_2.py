import csv
import matplotlib.pyplot as plt
import numpy as np

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/gdelt_conflict_1_0.csv")
data_reader = csv.DictReader(data_raw)
conflict_dataset = list(data_reader)
data_raw.close()

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/suicides.csv")
data_reader = csv.DictReader(data_raw)
suicide_dataset = list(data_reader)
data_raw.close()

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

# years = []
# for yr in suicide_dataset:
#     if yr["year"] not in years:
#         years.append(yr["year"])
# years.sort()

country_names = []
total_events = []
total_years = []


# This function compiles a chronological list of the total events of the specified country. This is used to efficiently
# populate the event information for each country.
def populate_events(country):
    year_tracker = []
    events = []
    for i in conflict_dataset:
        if i["CountryName"] == country and i["Year"] not in year_tracker:
            events.append(int(i["TotalEvents"]))
            year_tracker.append(i["Year"])
    return events


conflict_dict = {}
for i in conflict_dataset:
    # List of all years
    if i["Year"] not in total_years:
        total_years.append(i["Year"])

    # Making Dictionaries for each country
    if i["CountryName"] not in country_names:
        country_names.append(i["CountryName"])
        key = str(i["CountryName"])
        conflict_dict[key] = {
            "Years": total_years,
            "Suicides": [],
            "Events": populate_events(key)
        }

for k, v in conflict_dict.items():
    print(k, "\n", v)

# plt.figure(0, tight_layout=True)
#
# x_vals = [x for x in country_names]
# y_vals = [y for y in total_events]
#
# plt.bar(x_vals, y_vals)
# plt.xticks(rotation=75, size=5)
# plt.yticks(size=5)
#
#
# plt.show()


# for s in suicide_dataset:
#     print(s['year'])

# suicide_data = {}
# c_names = []
# suicide_rates = []
# for s in suicide_dataset:
#     if s['country'] not in c_names:
#         c_names.append(s['country'])
# print(c_names)
