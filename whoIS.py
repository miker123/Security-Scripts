#!/usr/bin/env python
#Author: Mike R
#Get the WhoIS information and present it in a way that can be of use.
import re
from bs4 import BeautifulSoup #BeautifulSoup to parse data
import urllib #URLLib to open website

#Can provide URLs to obtain who info from a file, or user. However wanted.
#ask user for domain
whoIS=raw_input('Which site to get whois info: ')

site='http://www.whois.com/whois/' + whoIS

#go to whois.com/whois/{user-defined-site}
html=urllib.urlopen(site)
bt=html.read()
soup=BeautifulSoup(bt, "lxml")

#dump data here
#could use .text to get data but want to be formatted
registryData=soup.findAll("div", {"id": "registryData"})
registryData=str(registryData)
clean=re.sub('<[^>]+>', '\n', registryData)
print clean

registrarData=soup.findAll("div", {"id": "registrarData"})
registrarData=str(registrarData)
clean2=re.sub('<[^>]+>', '\n', registrarData)
print clean2
