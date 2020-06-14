'''
The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML
data, compute the sum of the numbers in the file. You are to look through all the <comment> tags and find the <count> values sum the 
numbers.

Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_618665.xml (Sum ends with 31)
'''

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

location = input('Enter Location:')
data = urllib.request.urlopen(location).read()
print('Retrieving ', location)
tree = ET.fromstring(data)
comm = tree.findall('comments/comment/count')
num_list = []
for item in comm:
	num_list.append(int(item.text))
print('Count: ', len(num_list))
print('Sum: ', sum(num_list))
