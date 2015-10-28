#!/usr/bin/env python
#Author: Mike R

#copies a specific file on a Linux based machine.
#Changes will need to be made if one wanted to get this to work on Windows
#Instead of simply coping the file, one could do other things

import os
import shutil

name=raw_input("Which file to look for (name and extension):")
path="/"


result = []
for root, dirs, files in os.walk(path):
    if name in files:
        result.append(os.path.join(root, name))
        print name
        #copies file the name testFile.py. Name can be changed to anything
        shutil.copyfile(name, "testFile.py")
