'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

# Import json library
import json

# Open and load eq_data.json file
infile = open("eq_data.json", "r")
eq_data = json.load(infile)

# Print out the number of earthquakes
print()
print("The number of earthquakes:")
print(len(eq_data["features"]))
print()

# Create eq_dict to record need dictionaries and each_dict to loop through each earthquake
eq_dict = {"earthquakes":[]}
each_dict = {}

# Use loop to extract location, magnitude, longitude, and latitude and append to eq_dict
for each in range(len(eq_data["features"])):
   if eq_data["features"][each]["properties"]["mag"] > 6:
      each_dict["Location"] = eq_data["features"][each]["properties"]["place"]
      each_dict["Magnitude"] = eq_data["features"][each]["properties"]["mag"]
      each_dict["Longitude"] = eq_data["features"][each]["geometry"]["coordinates"][0]
      each_dict["Latitude"] = eq_data["features"][each]["geometry"]["coordinates"][1]
      eq_dict["earthquakes"].append(each_dict)
      each_dict = {}

# Print out eq_dict
print()
print(eq_dict)
print()

# Create keys_list for new eq_dict keys
keys_list = list(eq_dict["earthquakes"][0].keys())

# Use a for loop to print out all information in eq_dict
for n in range(len(eq_dict["earthquakes"])):
   print()
   print(keys_list[0] + ": " + eq_dict["earthquakes"][n]["Location"])
   print(keys_list[1] + ": " + str(eq_dict["earthquakes"][n]["Magnitude"]))
   print(keys_list[2] + ": " + str(eq_dict["earthquakes"][n]["Longitude"]))
   print(keys_list[3] + ": " + str(eq_dict["earthquakes"][n]["Latitude"]))
   print()

# Close infile
infile.close()