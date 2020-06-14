'''
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the
JSON data, compute the sum of the numbers in the file and enter the sum below: We provide two files for this assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_618666.json (Sum ends with 28)
'''

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
