#!/usr/bin/env python
#Author: Mike R
#Gets all Windows hotfixes that have been downloaded and writes to file

import os

try:
  #send data to files
	os.system("REG QUERY '"'HKLM\Software\Microsoft\Windows\CurrentVersion\Component Based Servicing\Packages'"' >test.txt") 
except:
	print "Unable to get the Windows Hotfixes"	
