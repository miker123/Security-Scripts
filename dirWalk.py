#!/usr/bin/env python
#Author: Mike R
#walking the current working directory
import os 
i=0
dash='---'
#ask user for directory or take it.

def dirWalk(thisDir, dash, i):
	i=i+1
	for item in os.listdir(thisDir):
		fullPath=os.path.join(thisDir,item)
		
		if os.path.isfile(fullPath):
			print (dash*i) + item
		elif os.path.isdir(fullPath):
			print (dash*i) + item
			newDir=thisDir + "/" + item
			dirWalk(newDir, dash, i)
		else:
			print "unknown!"		
#see if there is a way to print the directory name, not necessarily full path
directory=raw_input("What directory do you want to walk: ")
#if one wanted to get all files, then one would need to be sudo

#This would be used if one wanted to walk current directory
#curDir=os.getcwd()

dirWalk(directory, dash, i)
