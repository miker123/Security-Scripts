#/usr/bin/env python
#Author: Mike R
#User gives IP and it tells if it's valid
import socket


addr=raw_input("What is the IP:")
try:
    socket.inet_aton(addr)
    print "Valid IP"
# legal
except socket.error:
    print("Not a valid IP")
