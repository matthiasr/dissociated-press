#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from time import sleep
from sys import argv
import cProfile as profile

if len(argv) == 1:
    infile = "PLOMDATA"
else:
    infile = argv[1]

DEBUG = False
N = 2
BENCHMARK = False

d = dp.dictionary(debug=DEBUG)
f = open(infile,"r")
input = f.readlines()
f.close()

def dissociate(d,input):
    for i, l in enumerate(input):
        if DEBUG:
            print l
        d.dissociate(l, N=N)
        if not BENCHMARK and i%100 == 0:
            print i
    return d

if BENCHMARK:
    profile.run('dissociate(d,input)')
else:
    dissociate(d,input)

if BENCHMARK:
    profile.run('for i in xrange(1000): d.associate()')
    exit(0)

if BENCHMARK: exit(0)

try:
    while 1:
        sentence = d.associate()

        if sentence not in input:
            print sentence
            sleep(1)

except KeyboardInterrupt:
    print "=== Enough! ==="
