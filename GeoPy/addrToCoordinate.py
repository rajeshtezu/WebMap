'''
 geocoding: converting addresses to laitude-longitude coordinates.
 Need to have internet connection while working with this module because it sends address to online service
 to get the coordinates.
'''

import pandas
from geopy.geocoders import Nominatim

df = pandas.read_json("supermarkets.json")

# Update Address column with complete address
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

# Create geocoder object Nominatim
nomObj = Nominatim(scheme="http")

# apply geocode  method on each address of Address column and store the value in newly created column Coordinates
df["Coordinates"] = df["Address"].apply(nomObj.geocode)

# Now filter the latitude and longitude and store them into new columns
df["latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
print(df)


