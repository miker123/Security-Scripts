#!/usr/bin/env Python
#Multi-Process Port Scanner
import socket
from multiprocessing import Pool


open_p, closed_p = [], []
reponse = ["OPEN PORTS","CLOSED PORTS","SCANNING PORTS","TYPE",
           "SCANNING","ADDRESS","NUMBER OF PROCESSES"]

target_ip = raw_input("{}: ".format(reponse[5]))
num_procs = int(raw_input("{}: ".format(reponse[6])))
ip = socket.gethostbyname(target_ip)
print "{0}:{1}\n".format(reponse[4],ip)

def scan(arg):
    target_ip, port = arg
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.11)
    result = sock.connect_ex((target_ip,port))
    if result == 0:
        sock.shutdown(2)
        return port, True
    else:
        return port, False
    sock.close

try:
    portStart=raw_input("Which port to start: ")
    portEnd=raw_input("Which port to end: ")
    
    portEnd=(int)(portEnd)
    portStart=(int)(portStart)
    
    ports = range(portStart, portEnd)
    pool = Pool(processes=num_procs)
    print "{}: ".format(reponse[2])
    
    for port, status in pool.imap_unordered(scan, [(target_ip, port)for port in ports]):
        print port,
        open_p.append(port)if status else closed_p.append(port)

    print "\n\n{}".format(reponse[0])
    for elements in open_p:
        print "{0} {1} :{2}".format(elements,reponse[3],socket.getservbyport(elements))
except:
    print "Improper port values. Please try again later"
