# JSONs - Javascript Object Notation
# Real-time Server to Browser Communication
# Human Readable
# Load JSON: json_data
import json

with open("../Dataset/Importing Data From Dataset/snakes.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])