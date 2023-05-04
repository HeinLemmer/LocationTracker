import phonenumbers
import opencage
import folium

from mynumber import number

from phonenumbers import geocoder

pepNumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepNumber, "en")
print(location)

from phonenumbers import carrier
serviceProvider = phonenumbers.parse(number)
print(serviceProvider)

from opencage.geocoder import OpenCageGeocode
key='8625a9b585c8468a870e67918bd30824'

geocoder = OpenCageGeocode(key)
queryLocation = str(location)
results = geocoder.geocode(queryLocation)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start= 10)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("phoneLocation.html")