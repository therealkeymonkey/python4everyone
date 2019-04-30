import json
import urllib.request, urllib.parse, urllib.error
#import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

url = input('Enter json Location: ')
print('Retrieving', url)
url = urllib.request.urlopen(url)
   
data = url.read().decode()
print(data)
print('Retrieved', len(data), 'characters')

info = json.loads(data)
#print(info)
# Need a for loop
total = 0
for n in info['comments']:
    print (n['count'])
    total = total + (n['count'])
print(total)

