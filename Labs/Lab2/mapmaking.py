import folium
import csv
# from Lab_2 import read_data


def read_data(path):
    data_raw = open(path)
    data_reader = csv.DictReader(data_raw)
    file = list(data_reader)
    data_raw.close()
    return file


placelist = read_data("/Users/tkmuro/PycharmProjects/tkProgramming/Labs/Lab2/countries.csv")

coords = [37.5131, 122.1204]

map = folium.Map(location=coords, zoom_start=2)


for place in placelist:
    print(place)
    if place['latitude'] != "" and place['longitude'] != "":
        place['latitude'] = float(place['latitude'])
        place['longitude'] = float(place['longitude'])
    print(place)
    print()

for place in placelist:
    coordinates = [place['latitude'], place['longitude']]

    folium.CircleMarker(
        radius=100000,
        location=[45.5244, -122.6699],
        popup=place['name'],
        color="crimson",
        fill=False,
    ).add_to(map)


map.save('my_map.html')
