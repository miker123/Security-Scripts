#!/usr/bin/env python
#Author: Mike R

from scapy.all import *

#creating list of WiFi APs
wifi_aps=[]

def packet_handler(pkt) :
    # if packet has 802.11 layer, and type of packet is Data frame
    if pkt.haslayer(Dot11):
        if pkt.type==0 and pkt.subtype == 8:
                if pkt.addr2 not in wifi_aps:
                        wifi_aps.append(pkt.addr2)
                        print "Wifi AP MAC: " + pkt.addr2 + " with SSID " + pkt.info

#Can change the interface. Either have user input or scan all interface
sniff(iface="eth0", prn=packet_handler)
