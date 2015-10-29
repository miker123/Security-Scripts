#!/usr/bin/env python
#Author: Mike R
#Prints all Windows registry to files

import os

try:
	os.system("reg query HKCR /S > HKCR.txt") #send data to files
except:
	print "HKCR Registry Values don't exit"	

try:
	os.system("reg query HKCC /S > HKCC.txt") #send data to files
except:	
	print "HKCC Registry Values don't exit"	

try:
	os.system("reg query HKU /S > HKU.txt") #send data to files
except:	
	print "HKU Registry Values don't exit"	

try:
	os.system("reg query HKCU /S > HKCU.txt") #send data to files
except:
	print "HKCU Registry Values don't exit"	

try:
	os.system("reg query HKLM /S > HKLM.txt") #send data to files
except:
	print "HKLM Registry Values don't exit"	
