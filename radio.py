#! /usr/bin/python

import re
import time
import urllib2
from bs4 import BeautifulSoup

#response = urllib2.urlopen('http://python.org/')
response = urllib2.urlopen('http://www.nrk.no/programoversikt/avansert/?p_artikkel_id=&p_forhandsvis_flg=0&p_format=HTML&p_type=prog&p_fom_dag=11&p_fom_mnd=9&p_fom_ar=2012&p_periode=dennedagen&p_p1=P1&p_soketekst=&p_knapp=Vis+nedenfor')
html = response.read()

soup = BeautifulSoup(html)

print soup.title.get_text()

starttimes = soup.find_all("td", "pubkl")
programs = soup.find_all("div", "pubprogtittel")

now = time.strftime("%H:%M")

print now

# for starttime, program in zip(starttimes,programs):
#     print starttime.get_text(), 'starts: ', program.get_text()
