import random
import folium
import webbrowser

# def generate_random_gps():
#    latitude = random.uniform(-90, 90)
#    longitude = random.uniform(-180, 180)
#    return latitude, longitude

# loc = generate_random_gps()
# print(loc)

scofflaw = (32.47342644196209, -84.98520475789635)

# Create a Map instance
m = folium.Map(
    location=scofflaw,
    control_scale=True,
    zoom_start=20
)

folium.Marker(
    scofflaw,
    icon=folium.Icon(icon='beer', prefix='fa', color='red'),
    popup="CPT Gorak is here!"
).add_to(m)




# Save the map to an HTML file
m.save('map.html')

# Add a marker for the GPS coordinates



# Open the map file in the default web browser

webbrowser.open('map.html')

