#!/usr/bin/env python
#Author: Mike R
#Allows user to read from a file and look for specific things
import os
import sys

#read from /var/log/messages
os.system("cat /var/log/syslog > newFile.txt")


#find all logs which pertain to USB and print selectively
usbFile=open('newFile.txt')
for line in usbFile:
	if "rsyslog" in line:
		print line
