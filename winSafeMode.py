#!/usr/bin/env python
#Author: Mike R
#Send user machine into Safe Mode

#Goal is to send users machine into the proper set of Safe Mode.
#Then restart the machine

import os

#Safe Mode:
os.system("bcdedit /set {default} safeboot minimal")

#Safe Mode with Networking:
os.system("bcdedit /set {default} safeboot network")


#Safe Mode with Command Prompt:
os.system("bcdedit /set {default} safeboot minimal")
os.system("bcdedit /set {default} safebootalternateshell yes")


#shutdown and reboot the entire system
os.system("shutdown /r /f /t 60")
