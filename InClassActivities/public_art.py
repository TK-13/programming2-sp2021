import folium
import csv

# Map all pieces of art in Chicago.
# Mark each piece, and display the piece's title when the marker is clicked.

data_raw = open("/Users/tkmuro/PycharmProjects/tkProgramming/Resources/parks_public_art.csv")
data_reader = csv.DictReader(data_raw)
data = list(data_reader)
data_raw.close()


names = []
lat_long = []
for i in data:
    names.append(i["ART"])
    lat_long.append(i["LOCATION"])

print(names)
print(lat_long)

lat_long = [pair.strip("()") for pair in lat_long]
print()
print(lat_long)

'''
map = folium.Map(location=[41.878113, -87.629799], zoom_start=9)

for item in names:

    folium.Marker(location=[41.9227, -87.6379],
                  popup="Parker",
                  icon=folium.Icon(color="blue", icon="times", prefix="fa")
                  ).add_to(map)
'''
