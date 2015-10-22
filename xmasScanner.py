#!/usr/bin/env python
#Author: Mike R

#Code an XMAS port scanner which takes an IP address and Port number as input.
#Output will be response received from the host

import logging, socket
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


#2 variables-->Destination IP and Port
ipDest = raw_input("What IP would you like to initiate the XMAS scan against: ")
portDest= raw_input("Which port: ")

#checking validity of the port
try:
	port=int(portDest)
except:
	print "The destination port must be an integer value."

#checking to see if destination port is valid
ipList = ipDest.split('.')
if (len(ipList) == 4 and port>=1 and port<=65535):
	try:
  #By using this code, you agree to use the code not in a malicious fashion
	#Getting the response
		XMAS = sr1(IP(dst=ipDest)/TCP(dport=port,flags="FPU"),timeout=7)
	    	if (str(type(XMAS))=="<type 'NoneType'>"):
	    		print "Open|Filtered"

	#A response of RST flag means that the port is closed.
		elif(XMAS.haslayer(TCP)):
	 	   if(XMAS.getlayer(TCP).flags == 0x14):
	        	print "Closed"

		elif(XMAS.haslayer(ICMP)):
		    if(int(XMAS.getlayer(ICMP).type)==3 and int(XMAS.getlayer(ICMP).code) in [1,2,3,9,10,13]):
	       		print "Filtered"
	#catching errors
	except:
		print "Please make sure that the IP Address is between 0.0.0.0-255.255.255.255"

elif (len(ipList) == 4):
	print "The port must be between 1-65535" 
else:
	print "The IP Address must be between 0.0.0.0-255.255.255.255"
