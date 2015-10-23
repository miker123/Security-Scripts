#!/usr/bin/env python
#Author: Mike R
#Simple handler to catch control c singals

import signal
import platform

def ctrlc_handler(signum, frm):
	print "Why kill me? We are just getting started!!"

def ctrlZ_handler(signum, frm):
	print "Why kill me? We are just getting started!!"

print "installing signal handler ..."
signal.signal(signal.SIGINT, ctrlc_handler)
signal.signal(signal.SIGTSTP, ctrlZ_handler)

print "done!"

while True:
	pass
