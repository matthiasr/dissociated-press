#!/usr/bin/env python


from datetime import datetime
from time import sleep
from sys import argv
import re

if len(argv) == 1:
  infile = "PLOMDATA.complete"
else:
  infile = argv[1]

f = open(infile,"r")

# Date: 4:53 PM May 19th, 2008
# Date: Sat Apr 25 09:54:24 +0000 2009

def parsedate(line):
    try:
        return datetime.strptime(re.sub(r"(st|nd|rd|th),", ",", line),"Date: %I:%M %p %b %d, %Y\n")
    except ValueError:# try:
        return datetime.strptime(line,"Date: %a %b %d %H:%M:%S +0000 %Y\n")
    
times = sorted([parsedate(line).time() for line in f if line[:6] == "Date: "])

f.close()

BINWIDTH = 1 #minutes

distr = {}
for d in times: 
    try: distr[(d.minute + d.hour*60)/(BINWIDTH)] += 1
    except KeyError: distr[(d.minute + d.hour*60)/(BINWIDTH)] = 1

distr_sum = sum(distr.values())
for i,n in distr.items():
    distr[i] = float(n)/distr_sum

print distr

