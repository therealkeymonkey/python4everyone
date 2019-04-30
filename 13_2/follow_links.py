import urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
count = input("Enter Count - ")
position = input("Enter Position - ")
html = urlopen(url, context=ctx).read()
parsed = BeautifulSoup(html, "html.parser")
tags = parsed('a')
#print(parsed)
count = int(count)
position = int(position)
n = 0
x = 0
#print(url)
# nested loop to feed the 3rd url back in x times
while x < count:
    for tag in tags:
        while n < position:
            url1 = (tag.get('href', None))
            n = n + 1
            #print(n)
            #print(url1)
            break
    x = x + 1
    #print(x)
    loophtml = urlopen(url1, context=ctx).read()
    loopparsed = BeautifulSoup(loophtml, "html.parser")
    tags = loopparsed('a')
    n = 0
print(url1)
