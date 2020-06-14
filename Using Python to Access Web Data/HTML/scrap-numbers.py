'''
The program will use urllib to read the HTML from the data files below, and parse the data, extracting numbers and compute the sum of the
numbers in the file. The file is a table of names and comment counts. You are to find all the <span> tags in the file and pull out the 
numbers from the tag and sum the numbers.
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_41649.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
sum = 0
for tag in tags:
    count += 1    
    sum += int(tag.contents[0])
print('Sum: ', sum)
