'''
The program will use urllib to read the HTML from the data files, extract the href= vaues from the anchor tags, scan for a tag that
is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report
the last name you find.

Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html (Find the link at position 3 (the first name is 1). Follow
that link. Repeat this process 4 times. The answer is the last name that you retrieve. Sequence of names: Fikret Montgomery Mhairade
Butchi Anayah Last name in sequence: Anayah)

Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Ikemsinachukwu.html
Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you
retrieve. Hint: The first character of the name of the last page that you will load is: R
'''

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
num = input('Enter count: ')
pos = input('Enter position: ')
print('Retrieving: ', url)

for times in range(int(num)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving: ', tags[int(pos)-1].get('href', None))
    url = tags[int(pos)-1].get('href', None)
