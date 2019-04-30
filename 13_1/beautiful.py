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
html = urlopen(url, context=ctx).read()
parsed = BeautifulSoup(html, "html.parser")

num = parsed('span')
numbers = int()
for line in num:
     nums = (line.contents[0])
     nums = int(nums)
     print(nums)
     numbers = numbers + nums
print(numbers)
