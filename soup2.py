# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
count = input('Enter Count : ')
count = int(count)
pos = input('Enter position : ')

# Retrieve all of the anchor tags
tags = soup('a')
print('Retrieving : ',url)
print('Retrieving : ',tags[int(pos)-1].get('href',None))
#print(tags[2].contents[0])


for i in range(count-1) :
    html = urllib.request.urlopen(tags[int(pos)-1].get('href',None), context=ctx)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving : ',tags[int(pos)-1].get('href',None))

print('Answer :', tags[int(pos)-1].contents[0])