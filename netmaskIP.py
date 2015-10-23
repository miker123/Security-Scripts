#!/usr/bin/env python
import netifaces
from netifaces import *

#Author: Mike R
#Get all of the interfaces on the machine and provides their IP and netmask addresses if they exist.
#Tested on Linux machine

#getting interface list
interface_list = netifaces.interfaces()

#use interface list to get list of interfaces to then get the addresses
interfaceNum= int(len(interface_list))
for i in range(interfaceNum):
    try:
        info=netifaces.ifaddresses(interface_list[i])[AF_INET]
        maskAddr=info[0]['netmask']
        ipAddr=info[0]['addr']
        print "Interface: " + interface_list[i] + " has an IP address of " + str(ipAddr) + " and a netmask of " +str(maskAddr)
    except:
        print "Interface: " + interface_list[i]
