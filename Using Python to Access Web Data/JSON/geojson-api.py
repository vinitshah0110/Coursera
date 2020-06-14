'''
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve
the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
Use this API endpoint that has a static subset of the Google Data: http://py4e-data.dr-chuck.net/json?
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is
properly URL encoded using the urllib.parse.urlencode() function

Test Data / Sample Execution
You can test to see if your program is working with a location of "South Federal University" which will have a place_id of 
"ChIJ0V94rPl_bIcRqLdrlbjFMDk".
'''

import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# If you have a Google Places API key, enter it here
# api_key = '' (https://developers.google.com/maps/documentation/geocoding/intro)

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = input('Enter location: ')
parms = dict()
parms['address'] = address
if api_key is not False: parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None
print(js['results'][0]['place_id'])
