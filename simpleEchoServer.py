#!/usr/bin/env python
#Author: Mike R
#Simple echo server that accepts 1 connection and echoes the data

import socket
tcpSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.bind(("0.0.0.0",8088))
tcpSocket.listen(2)
print "Waiting for a client...."
(client, (ip,sock))=tcpSocket.accept()
print "Received connection from :",ip
print "Starting ECHO output ..."
data = 'dummy'
while len(data):
	data=client.recv(2048)
	print "Client sent:", data
	client.send(data)

print "Closing Connection ...."
client.close()
