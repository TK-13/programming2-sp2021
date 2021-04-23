import csv
import matplotlib.pyplot as plt
import folium

# Empty lists, which will be rewritten later. total_years is specified, because the suicide dataset contains data for
# a specific set of years.
country_names = []
total_events = []
total_years = [2000, 2010, 2015, 2016]
center_coordinates = [37.5131, 122.1204]


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


# Borrowed this function from Lab 1 for users to select a country to graph.
def user_input(message, param_list):
    user_entry = ""
    while user_entry not in param_list:
        user_entry = input(message)
    return user_entry


# Using read_data() to read the respective datasets into dictionaries
new_suicide_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/Age-standardized suicide rates.csv")
coordinate_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/countries.csv")
place_list = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/countries.csv")
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


# Making Dictionaries for each country, all nested within an overall dictionary.
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

# Graphing suicide rates and total conflicts over time for any arbitrary country. Graphing 2 types of data
# for every country would be a nightmare, so I had to go one at a time.
plt.figure(0, tight_layout=True)
print(country_names)
target = user_input("Select a country: ", country_names)

x_key = 'Years'
y_key_1 = 'Suicide Rates'
y_key_2 = 'Events'
x_values = [x for x in country_dict[target][x_key]]
y1_values = [y * (10 ** 4) for y in country_dict[target][y_key_1]]
# Suicide rates are multiplied like so for easier reading on the graph. Otherwise it looked horizontal.
# consider not manipulating the data.
y2_values = [y for y in country_dict[target][y_key_2]]

plt.plot(x_values, y1_values, color="red", label='Suicide Rates')
plt.plot(x_values, y2_values, color="blue", label='Total Events')
plt.title('Suicide Rates and Total Events of ' + target + ' over Time')
plt.xlabel(x_key)
plt.ylabel("Total Events (10^6) and\nSuicide Rates (10^4 for easy viewing)")
plt.legend()
# plt.xticks(rotation=75, size=5)
# plt.yticks(size=5)
plt.show()

# Finding correlation between conflict and suicides
# for every country:
# find overall change in conflicts, suicides
# the smaller the difference, the bigger the radius
# the greater the difference, the smaller the radius (correlation)

# Mapping correlation between conflict and suicides geographically.
circle_map = folium.Map(location=center_coordinates, zoom_start=2)
for place in place_list:
    if place['latitude'] != "" and place['longitude'] != "":
        place['latitude'] = float(place['latitude'])
        place['longitude'] = float(place['longitude'])

    coordinates = (place['latitude'], place['longitude'])

    folium.CircleMarker(
        radius=100,
        location=coordinates,
        popup=place['name'],
        color="crimson",
        fill=False,
    ).add_to(circle_map)

circle_map.save('my_map.html')
