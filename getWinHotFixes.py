#!/usr/bin/env python
#Author: Mike R

#gets hotfix information on Windows OS and writes to a file on the disk in the current working directory

import os

os.system("REG QUERY \"HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Component Based Servicing\\Packages\" >test.txt")
