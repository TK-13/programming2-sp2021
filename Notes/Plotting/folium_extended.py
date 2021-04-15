import folium
import csv

# https://python-visualization.github.io/folium/quickstart.html#

art_map = folium.Map(location=[41.8781, -87.6298], zoom_start=11)

# Parker 41.923000, -87.638461
# placing a marker on the map
folium.Marker(location=[41.923000, -87.638461],
              popup="Our School",
              icon=folium.Icon(color='red', icon='graduation-cap', prefix='fa'),
              ).add_to(art_map)

art_map.save('my_artmap.html')

"""
marker options:

with prefix='fa': https://fontawesome.com/v4.7.0/icons/ 
(https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css)

without: https://getbootstrap.com/docs/3.3/components/

"""


# open the file and read through it
import csv
import random

art_file = open("/Users/bifft/PycharmProjects/programming2-sp2021/Resources/parks_public_art.csv")
art_data = list(csv.DictReader(art_file))

color_list = ['darkgreen', 'gray', 'lightgreen', 'darkpurple', 'cadetblue', 'lightblue', 'lightgray', 'orange', 'darkred', 'purple', 'pink', 'black', 'darkblue', 'beige', 'lightred', 'green', 'blue']

# make separate lists for art, location
for i in art_data:
    folium.Marker(location=[i["LATITUDE"], i["LONGITUDE"]],
                  popup="<b>{0}</b>".format(i["ART"]),
                  icon=folium.Icon(color=random.choice(color_list), icon="cubes", prefix="fa")).add_to((art_map))

# plot the data from there
art_map.save('my_artmap.html')