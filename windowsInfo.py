#!/usr/bin/env python
#Author: Mike R

#Get Information about the host machine

import os

#Get System Information	and write to a file for later analysis
os.system("msinfo32 /report C:\TEMP\test.txt");

#Get Scheduled Tasks and write to a file for later analysis
os.system("SCHTASKS /Query > scheduled.txt");

#Get Services Running and write to a file for later analysis
os.system("sc query > sc.txt");

#Get a List System Configuration and write to a file for later analysis
os.system("systeminfo > systeminfo.txt");


#Get Tasklist and write to a file for later analysis
os.system("tasklist > tasklist.txt");
