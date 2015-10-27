#!/usr/bin/env python
#Author: Mike R
#Provides method of obtaining PIDS for a Linux/Unix system and prints to the cmd. Can be manipulated to use in other ways as well

import subprocess
ps = subprocess.Popen("ps -U 0", shell=True, stdout=subprocess.PIPE)
print ps.stdout.read()
ps.stdout.close()
