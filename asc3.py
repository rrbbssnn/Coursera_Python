import re
import socket
import urllib
from BeautifulSoup import *
import xml.etree.ElementTree as ET
import json

# for assignment 2 of Using Python to Access Web Data

#file = open('regex_sum_227189.txt')
#sum = 0
#for line in file:
#   numbersPerLine = re.findall('[0-9]+', line)
#   for n in numbersPerLine:
#   	sum = sum + int(n)
#print sum

# for assignment 3 of Using Python to Access Web Data

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.pythonlearn.com', 80))
# mysock.send('GET /code/intro-short.txt HTTP/1.1\n')
# mysock.send('Host: www.pythonlearn.com\n\n')

# while True:
#     data = mysock.recv(512)
#     if ( len(data) < 1 ) :
#         break
#     print data;

# mysock.close()

# for assignment 4-1 of Using Python to Access Web Data

# soup = BeautifulSoup(urllib.urlopen('http://python-data.dr-chuck.net/comments_227194.html').read())

# sum = 0
# # Retrieve all of the span tags
# tags = soup('span')
# for tag in tags:
#     # Look at the parts of a tag
#     sum = sum + int(tag.string)
# print sum

# for assignment 4-2 of Using Python to Access Web Data
# url = raw_input('Type your url: ')
# count = int(raw_input('Type your count value: '))
# po = int(raw_input('Type you\'d like to start from which name: '))

# while count >= 1 :
# 	c = po
#  	soup = BeautifulSoup(urllib.urlopen(url).read())

#  	for tag in soup('a'):
# 		c = c - 1
# 		if c >= 1 : continue
# 		else : 
# 			print tag.contents[0]
# 			url = tag.get('href', None)
# 			break

# 	count = count - 1

# for assignment 5 of Using Python to Access Web Data
# url = 'http://python-data.dr-chuck.net/comments_227191.xml'
# data = urllib.urlopen(url).read()
# tree = ET.fromstring(data)
# sum = 0
# counts = tree.findall('.//count')
# for count in counts:
# 	sum = sum + int(count.text)
# print sum

# for assignment 6-1 of Using Python to Access Web Data

# url = 'http://python-data.dr-chuck.net/comments_227195.json'
# data = urllib.urlopen(url).read()
# info = json.loads(str(data))
# sum = 0
# for item in info['comments']:
# 	sum = sum + int(item['count'])
# print sum

# for assignment 6-2 of Using Python to Access Web Data

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    # print json.dumps(js, indent=4)

    pid = js["results"][0]["place_id"]
    addr = js["results"][0]["formatted_address"]
    print 'Location: ',addr,'place_id',pid
    