import folium

map = folium.Map(location=[41.9227, -87.6379], zoom_start=9)

folium.Marker(location=[41.9227, -87.6379],
              popup="Parker",
              icon=folium.Icon(color="blue", icon="times", prefix="fa")
              ).add_to(map)

"""
marker options:

with prefix='fa': https://fontawesome.com/v4.7.0/icons/ 
(https://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css)

without: https://getbootstrap.com/docs/3.3/components/

"""

map.save('my_map.html')