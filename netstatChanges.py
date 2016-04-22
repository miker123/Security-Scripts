#!/usr/bin/env python
import difflib
import sys

#loading first file this should be the file from last review
with open('netstat.txt') as f:
    t1 = f.read().splitlines()
    t1s = set(t1)

#loading first file this should be the file from current review
with open('netstat2.txt') as f:
    t2 = f.read().splitlines()
    t2s = set(t2)

#in last file but not this one. This means connections have been removed.

print "Connections that have been removed between assessments\n"
for diff in t1s-t2s:
    print t1.index(diff), diff

print "----------------------------------------------------------------\n"

print "Connections that have been added between assessments"

#in this file but not last one. This means new connections have been added.
for diff in t2s-t1s:
    print t2.index(diff), diff


print "\n"
print "No results, means there have been no changes to the netstat table since the last assessment"
