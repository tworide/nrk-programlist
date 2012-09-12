#! /usr/bin/python

import re
import time
import urllib2
from bs4 import BeautifulSoup
import urlutils
import sys

#response = urllib2.urlopen('http://python.org/')

urlbuild = urlutils.UrlBuilder(query='p_format=HTML')
plist = urlutils.ProgramListParams()
print sys.argv[1]

day = time.strftime("%d")
month = time.strftime("%m")
year = time.strftime("%Y")

print day, month, year

plist.setChannel(sys.argv[1])
plist.setFomDag(day)
plist.setFomMnd(month)
plist.setFomAr(year)

urlbuild.setQuery(plist)

response = urllib2.urlopen(urlbuild.__str__())
html = response.read()

soup = BeautifulSoup(html)

print soup.title.get_text()

starttimes = soup.find_all("td", "pubkl")
programs = soup.find_all("div", "pubprogtittel")

now = time.strftime("%H:%M")

for starttime, program in zip(starttimes,programs):
    print starttime.get_text(), 'starts: ', program.get_text()
