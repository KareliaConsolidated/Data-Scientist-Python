# What is an API ?
# Set of Protocols and Routines
# Allows two software programs to communicate with each other.

import requests
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=hackers'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
	print(key + ':', value)

# APIs and interacting with the World Wide Web
# http: making an http request
# www.omdbapi.com - querying the OMDB API
# ?t=hackers
	# Query String
# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)

# JSON–from the web to Python

# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

#====================Another API Request=========================#
# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)
