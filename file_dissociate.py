#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from time import sleep
from sys import argv

if len(argv) == 1:
    infile = "TESTDATA"
else:
    infile = argv[1]

d = dp.dictionary()
f = open(infile,"r")
input = f.readlines()
f.close()

for l in input:
    print l
    d.dissociate(l)

try:
    while 1:
        sentence = d.associate()

        if sentence not in input:
            print sentence
        else:
            print "FAIL:", sentence

        sleep(1)

except KeyboardInterrupt:
    print "=== Enough! ==="
