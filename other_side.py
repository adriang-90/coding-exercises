from folium import Map, Marker, Popup
from geo import Geopoint

# Get latitude and longitude values
latitude = 40.4
longitude = -3.7

# Folium Map instance
mymap = Map(location=[latitude, longitude])

# Create a Geopoint instance
geopoint = Geopoint(latitude=latitude, longitude=longitude)
forecast = geopoint.get_weather()

popup_content = f"""
{forecast[0][0][-8:-6]}h: {round((forecast)[0][1])}
<img src="http://openweathermap.org/img/wn/{forecast[0][-1]}@2x.png" width=35>
<hr style="margin:1px">
{forecast[0][0][-8:-6]}h: {round((forecast)[1][1])}
<img src="http://openweathermap.org/img/wn/{forecast[1][-1]}@2x.png" width=35>
<hr style="margin:1px">
{forecast[0][0][-8:-6]}h: {round((forecast)[2][1])}
<img src="http://openweathermap.org/img/wn/{forecast[2][-1]}@2x.png" width=35>
<hr style="margin:1px">
{forecast[0][0][-8:-6]}h: {round((forecast)[3][1])}
<img src="http://openweathermap.org/img/wn/{forecast[3][-1]}@2x.png" width=35>
<hr style="margin:1px">
"""

# Create a Popup object and add it to Geopoint
popup = Popup(popup_content, max_width=400)
popup.add_to(geopoint)
geopoint.add_to(mymap)

# Save the Map instance into a HTML file
mymap.save("map.html")
