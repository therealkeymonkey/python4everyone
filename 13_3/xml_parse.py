import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter XML Location: ')
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
#print('Number of comments:', len(count))
#count = int(0)
sum = int()
for item in lst:
   count = item.find('count').text
   count = int(count)
   sum = sum + count
print(sum)
