import urllib.request, urllib.parse, urllib.error
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

location = input('Enter location: ')
print('Retrieving ', location)
num_list = []
data = urllib.request.urlopen(location).read()
print('Retrieved ', len(data))

info = json.loads(data)
info = info['comments']
for item in info:
	num_list.append(int(item['count']))
print('Count: ', len(num_list))
print('Sum: ', sum(num_list))