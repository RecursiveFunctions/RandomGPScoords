Toy project:
Provide a random GPS coordinate every few hours to simulate the location of a target such that whenever someone asks "WHERE IS HE???" you will instantly have an answer.


A GPS coordinate is valid (as in exists somewhere on Earth) as long as the latitude is between -90 to 90 and longitude is between -180, 180.

We could generate completely random GPS coordinates by using the following code:
```PYTHON TI: "Random GPS coordinate Generator"HL:"4,5" "fold"
import random

def generate_random_gps():
   latitude = random.uniform(-90, 90)
   longitude = random.uniform(-180, 180)
   return latitude, longitude

print(generate_random_gps())
```

We can use folium to generate a map and see where it lands. 
I kept running into import issues with folium, and for whatever reason, using specifically `pip3 install folium` worked for me. 

```python
import folium

# Create a Map instance
m = folium.Map(location=[lat, lon], zoom_start=13)

# Add a marker for the GPS coordinates
folium.Marker([lat, lon]).add_to(m)

# Display the map
m

```


if you run the above code it doesn't actually display anything as a standalone script. We need to save it to an HTML file and open that in a browser.

```python
# Save the map to an HTML file
m.save('map.html')

# Open the map file in the default web browser
import webbrowser

webbrowser.open('map.html')
```

![[Pasted image 20231127224133.png]]

Let's try a business and mark it with a symbol this time.
```python
#I'm going to use a discrete location this time
scofflaw = (32.47342644196209, -84.98520475789635)

# Create a Map instance
m = folium.Map(
    location=scofflaw,
    control_scale=True,
    zoom_start=20 #The higher this number, the closer the zoom
)

  

folium.Marker(
    scofflaw,
    icon=folium.Icon(icon='beer', prefix='fa', color='red'),
    popup="CPT Gorak is here!"

).add_to(m)
```

all of that should come before the following (otherwise you'll be making changes after the map has already been displayed)
```python
m.save('map.html')
webbrowser.open('map.html')
```

![[Pasted image 20231127225025.png]]

This added a red beer icon from font-awesome and if you click on it, the popup text will show
![[Pasted image 20231127225214.png]]

