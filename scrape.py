#!/usr/bin/python

import urllib2
import pandas as pd
from bs4 import BeautifulSoup
from pprint import pprint

url='http://192.168.254.254/cgi-bin/devices.ha'
contents=urllib2.urlopen(url)

soup = BeautifulSoup(contents, 'lxml') # Parse the HTML as a string
table = soup.find_all( "table", {"class":"table100"} )[1]

new_table = []

row_marker = 0
for row in table.find_all('table'):
    columns = row.find_all('tr')
    name = columns[0].find_all('td')[1].find('div').get_text().strip()
    mac = columns[0].find_all('td')[2].get_text().strip()
    ip = columns[2].find_all('td')[0].get_text().strip()
    status = columns[3].find_all('td')[1].get_text().strip().split('\n')[1]
    record = {'name':name, 'mac':mac, 'ip':ip, 'status':status}
    new_table.append(record)

pprint(new_table)
