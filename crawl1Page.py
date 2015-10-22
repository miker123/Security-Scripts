#!/usr/bin/env python
#Author: Mike R
#This will ask the user for a website to crawl and then get the URLs for that page. 
#Will only go for that layer. Won't go any deeper.


import mechanize
from bs4 import BeautifulSoup
import collections
from urlparse import urlparse 
import os


# Browser
br = mechanize.Browser()

#arrays to work with
urlArray=[]
uniqueURLS=[]
newSite=[]
allSites=[]

filePath=os.getcwd()
curFile=filePath+ 'urlLinks.txt'

#open file for writing to make output easier
file_object = open('urlLinks.txt', 'a')


def siteCrawl(site):
	br.open(site)
	file_object.write("---------------------------------------------------------------")
	file_object.write("\n")
	file_object.write(site)
	file_object.write("\n")
	file_object.write("---------------------------------------------------------------")
	file_object.write("\n")
	goHTML=br.response().read()
	for link in br.links():
		#Maybe write this to a file to keep the screen clean and preserve data
		file_object.write(link.text)
		file_object.write("\t")		
		file_object.write(link.url)
		file_object.write("\n")

		#getting list of all of the sites
		allSites.append(link.url)
		
		#print out stats about which site links are in the url.
		parsed=urlparse(link.url)
		#get data and put into array.
		urlArray.append(parsed.netloc)
		

def uniqueSites(urlArray, site):

	#remove duplicates from array
	uniqueURLS=(list(set(urlArray)))
	file_object.write("---------------------------------------------------------------")
	file_object.write("\n")
	sentence= "The site " + site + " contains links to:"
	file_object.write(sentence)
	file_object.write("\n")
	file_object.write("---------------------------------------------------------------")
	file_object.write("\n")
	
	for i in range(0,len(uniqueURLS)):
		#Maybe write this to a file to keep the screen clean and preserve data
		file_object.write(uniqueURLS[i])
		file_object.write("\n")
		newSite.append(uniqueURLS[i])

urlToCrawl=raw_input("Which Site to Crawl:")

#checking to see if HTTPS/HTTP/ or needs that to be added before going and crawling the address
if "http://www." in urlToCrawl:
	siteCrawl(urlToCrawl)
elif "https://www." in urlToCrawl:
	siteCrawl(urlToCrawl)
elif "www." in urlToCrawl:
	try:	
		urlToCrawl="http://" + urlToCrawl
		siteCrawl(urlToCrawl)

	except:
		urlToCrawl="https://" + urlToCrawl
		siteCrawl(urlToCrawl)
elif "www." not in urlToCrawl:
	try:	
		urlToCrawl="http://" + urlToCrawl
		siteCrawl(urlToCrawl)

	except:
		urlToCrawl="https://" + urlToCrawl
		siteCrawl(urlToCrawl)	

#getting unique sets that have been visited
uniqueSites(urlArray, urlToCrawl)
#works once, but needs a way to work every time.
#maybe easier way to show up?
#Unique sites as well?

#add in which site was linked to the most?
for number in range(0,len(allSites)):
	#count per site
	print number
	try:
		if "http://www." in allSites[number]:
			siteCrawl(allSites[number])
			uniqueSites(urlArray, urlToCrawl)
		elif "https://www." in urlToCrawl:
			siteCrawl(allSites[number])		

		else:
			newSite=urlToCrawl+allSites[number]
			siteCrawl(newSite)

	except:
		print "Didn't work"
