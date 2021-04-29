import csv
import matplotlib.pyplot as plt
import folium

# Empty lists, which will be rewritten later. total_years is specified, because the suicide dataset contains data for
# a specific set of years.
country_names = []
total_events = []
total_years = [2000, 2010, 2015, 2016]
center_coordinates = [0, 0]
RUNS = 0


# This function is meant to compile a chronological list of the total events of the specified country.
# This is used to efficiently populate the event information for each country.
def populate_events(country):
    year_tracker = []
    events = []
    for c in conflict_dataset:
        if c["CountryName"] == country and int(c['Year']) in total_years and c["Year"] not in year_tracker:
            events.append(int(c["TotalEvents"]))
            year_tracker.append(c["Year"])
    return events


# This function works similarly a the previous one, but returns a list of suicide rates by year.
def populate_suicides(country):
    suicide_rates = []
    for s in new_suicide_dataset:
        if s["Country"] == country and s["Sex"] == " Both sexes":
            for t in total_years:
                suicide_rates.append(float(s[str(t)]))  # The values of total_years are ints, so in order for
                # this to work as a key for new_suicide_dataset, it must be a string.
    return suicide_rates


# This function is just mean to make it easier to put the datasets into a dictionary.
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


# This function is part of my attempt to determine correlation between suicide rates and violent events.
# It finds the average rate of change of a value (whether that's suicide rate or conflicts) from
# 2000 to 2016. Although crude, it was my best idea for determining whether the data correlated.
# If I have time, I could try taking instantaneous rate of change for each year, to see if the conflicts and
# suicides have similar slopes yearly.
def rate_of_change(country, key):
    return float((country_dict[country][key][3] - country_dict[country][key][0]) / 16)


# Developed in the dataset_sorting file, this function makes it easier to sort through all datasets using
# one country_names list. In order to do that, I had to rename certain countries within a target dataset to a
# specified key (Example: a unique country name like "Bahamas, The" is replaced with "Bahamas", to match
# the country list)
def country_rename(target_dataset, key, target_name, replacement_name):
    for row in target_dataset:
        if row[key] == target_name:
            row[key] = replacement_name


# This function is supposed to make two graphs for the target country; suicide rates over time, and total conflicts
# over time.
def line_graph(figure_no, target_country, x_key, y_key, color):
    plt.figure(figure_no, tight_layout=True)
    x_values = [x for x in country_dict[target_country][x_key]]
    y_values = [y for y in country_dict[target_country][y_key]]
    plt.plot(x_values, y_values, color=color)
    plt.title(y_key + ' of ' + target_country + ' over Time')
    plt.ylabel(y_key)


# Using read_data() to read the respective datasets into dictionaries
new_suicide_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/Age-standardized suicide rates.csv")
coordinate_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/countries.csv")
conflict_dataset = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/gdelt_processor_friendly.csv")
# The 'processor friendly' version only has data beyond the year 2000, since that's roughly the range of
# the suicide data. This way, the program can spend less time looking through all 176k lines of the original
# dataset, while still having to sort through and find the right values, as it normally would.


# Renaming:
# All renames have to happen before the dictionary is made, so the key in the suicides dataset (and subsequently
# the country names list) matches the key in the conflict dataset).
# The target_list and replacement_list generation probably could have been automated with some loops and string
# parsing, but I didn't have time to look into that.
target_list = ['Bahamas',
               'Bolivia (Plurinational State of)',
               'Brunei Darussalam',
               "Congo",
               "Democratic Republic of the Congo",
               'Cabo Verde',
               "Côte d'Ivoire",
               'Czechia',
               'Iran (Islamic Republic of)',
               "Lao People's Democratic Republic",
               'Syrian Arab Republic',
               'Eswatini',
               "United Kingdom of Great Britain and Northern Ireland",
               'United Republic of Tanzania',
               'United States of America',
               "Venezuela (Bolivarian Republic of)",
               "Viet Nam",
               'Gambia',
               'Micronesia (Federated States of)',
               "Democratic People's Republic of Korea",
               "Republic of Korea",
               "Republic of Moldova",
               "Republic of North Macedonia",
               "Russian Federation"]  # The names of certain, misnamed countries within the suicide dataset

replacement_list = ['Bahamas, The',
                    'Bolivia',
                    "Brunei",
                    "Congo, Democratic Republic of the",
                    "Congo, Democratic Republic of the",
                    'Cape Verde',
                    "Cote d'Ivoire",
                    'Czech Republic',
                    'Iran',
                    "Laos",
                    'Syria',
                    "Swaziland",
                    "United Kingdom",
                    "Tanzania",
                    "United States",
                    "Venezuela",
                    "Vietnam",
                    "Gambia, The",
                    "Micronesia, Federated States of",
                    "Korea, North",
                    "Korea, North",
                    "Moldova",
                    "Macedonia",
                    "Russia"]  # The name of that same country within the gdelt dataset.

# This is supposed to go through the suicide dataset and rename all the countries specified in target_list
# with their 'correct' name from the replacement list.
for r in range(len(target_list)):
    country_rename(new_suicide_dataset, 'Country', target_list[r], replacement_list[r])
# extra line for the Democratic Republic of Congo because it had two names within gdelt too.
country_rename(conflict_dataset, 'CountryName', 'Congo, Republic of the', 'Congo, Democratic Republic of the')
print("Anomalous countries renamed.")
print()


# Making Dictionaries for each country, all nested within an overall dictionary.
# Ms. Ifft suggested making a dictionary of all countries, and to make sub-dictionaries within each country
# containing lists for violent events, years, etc. This code is meant to accomplish that.
country_dict = {}
for i in new_suicide_dataset:
    name = i["Country"]
    if name not in country_names:
        country_names.append(name)
        key = str(name)
        country_dict[key] = {
            "Years": total_years,
            "Suicide Rates": populate_suicides(key),
            "Events": populate_events(key),
            "Coordinates": (0, 0),
            "Difference": 0.0
        }
print("Dictionaries made.")
print()

# This is supposed to find correlation between conflict and suicides for every country. I thought that, if the
# average rate of change of the two is similar, there must be better correlation. Vice-versa, if the avg. rates
# of change are different, there probably wasn't a connection.
for country in country_names:
    delta_suicides = rate_of_change(country, "Suicide Rates")
    delta_conflicts = rate_of_change(country, "Events")
    difference = abs(delta_conflicts - delta_suicides)
    country_dict[country]['Difference'] = difference
print("Difference in rate of change data added.")
print()

# Adding coordinate data to dictionary. Country names were confirmed to align in dataset_sorting.
for place in coordinate_dataset:
    if place['latitude'] != "" and place['longitude'] != "":
        place['latitude'] = float(place['latitude'])
        place['longitude'] = float(place['longitude'])

        coordinates = (place['latitude'], place['longitude'])
        if place['name'] in country_names:
            country_dict[place['name']]['Coordinates'] = coordinates
print("Coordinate data added.")
print()


# Mapping correlation between conflict and suicides geographically.
proceed_map = user_input("\nMap correlation? [y/n]: ", ['y', 'n'])
if proceed_map == 'y':
    circle_map = folium.Map(location=center_coordinates, zoom_start=2)
    for place in country_dict:
        dummy_radius = ((country_dict[place]['Difference']) / 10)
        dummy_color = "orange"
        msg = (place +
               ": \nSuicide rate: " + str(country_dict[place]['Suicide Rates']) +
               "\nTotal Events: " + str(country_dict[place]['Events']))

        # This section is supposed to color code the circle marker for each country, by how great the difference is
        # in rate of change of suicide rates vs conflicts. The smaller the difference, the darker the color.
        # This just makes it easier to identify which regions have particularly strong correlation.
        # Countries with massive differences are replaced by a red dot, to avoid overcrowding the map.
        if country_dict[place]['Difference'] <= 600.0:
            dummy_color = "yellow"
        if country_dict[place]['Difference'] <= 500.0:
            dummy_color = "green"
        if country_dict[place]['Difference'] >= 1000.0:
            dummy_radius = 2
            dummy_color = "crimson"
            msg = (place + "\nDifference too large to show.")

        folium.CircleMarker(
            radius=dummy_radius,
            location=(country_dict[place]['Coordinates']),
            popup=msg,
            color=dummy_color,
            fill=False,
        ).add_to(circle_map)

    circle_map.save('lab2_map.html')


# Graphing suicide rates and total conflicts over time for any chosen country.
# Even though it's technically my first graph, I put it second in order so that, once the user has reviewed the
# global data, they can then look at the graph for a particular country of their choosing.
proceed_graphing = user_input("\nGraph a country's data? [y/n]: ", ['y', 'n'])
if proceed_graphing == 'y':
    done = False
    while done != 'True':
        if RUNS > 0:
            done = user_input("Finished? [True, False] ", ['True', 'False'])
            # This "game loop" is in place so that users can look at as many graphs as they want, rather than having
            # to re-run the whole program each time.
        if done != 'True':
            print()
            print(country_names)
            target = user_input("Select a country: ", country_names)
            line_graph(0, target, 'Years', 'Suicide Rates', 'red')
            line_graph(1, target, 'Years', 'Events', 'blue')
            RUNS += 1

            plt.show()
