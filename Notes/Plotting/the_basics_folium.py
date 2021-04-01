import folium

map = folium.Map(location=[50.075539, 14.437800], zoom_start=9)

folium.Marker(location=[50.087811, 14.420460],
              popup="Prague Castle",
              icon=folium.Icon(color="green", icon="flag", prefix="fa")
              ).add_to(map)

"""
marker options:

with prefix='fa': https://fontawesome.com/v4.7.0/icons/ 
(https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css)

without: https://getbootstrap.com/docs/3.3/components/

"""

map.save('my_map.html')