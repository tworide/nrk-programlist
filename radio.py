#! /usr/bin/python

import re
import argparse
from datetime import datetime, timedelta, time
import urllib2
from bs4 import BeautifulSoup
import urlutils
import sys

parser = argparse.ArgumentParser(description='List shows for spesific radio channel',
                                 epilog='For info contact toij@ifi.uio.no',
                                 prog='Channel Program Listing')
parser.add_argument('-v','--version', action='version', version='%(prog)s 0.1')
parser.add_argument('-c','--channel', required=True, 
                    help='The name of the channel to list programs for',
                    action='store')
parser.add_argument('-d','--days-from-today', type=int, help='Specify # days from today for listing of that day', default=0)
args = parser.parse_args()
print "Channel:", args.channel

urlbuild = urlutils.UrlBuilder(query='p_format=HTML')
plist = urlutils.ProgramListParams()

now = datetime.now()
print args
now = now + timedelta(days=args.days_from_today)

day = now.day
month = now.month
year = now.year

print day, month, year

plist.setChannel(args.channel)
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

for starttime, program in zip(starttimes,programs):
    timestamp = starttime.get_text()
    hours = int(timestamp[:2])
    minutes = int(timestamp[-3:])
    hm = time(hours, minutes)
    dpcomp = datetime.combine(now, hm)

    if now < dpcomp:
        print starttime.get_text(), 'starts: ', program.get_text()
