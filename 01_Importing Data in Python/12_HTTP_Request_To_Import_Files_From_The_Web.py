# HTTP
# Hyper Text Transfer Protocol
# Foundation of data communication for the web
# HTTPS - more secure form of HTTP
# Going to a website = sending HTTP request
	# Get Request
# urlretrieve() performs a GET request

# GET requests using urllib
from urllib.request import urlopen, Request
url = "http://www.wikipedia.org/"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()

# GET requests using requests

import requests
url = "http://www.wikipedia.org/"
r = requests.get(url)
print(r.text)