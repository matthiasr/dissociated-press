#!/usr/bin/python
# -*- coding: utf-8 -*-

import dissociated_press as dp
from sys import argv
import cProfile as profile

if len(argv) == 1:
    infile = "PLOMDATA"
else:
    infile = argv[1]

N = 2

d = dp.dictionary(debug=False)
f = open(infile,"r")
input = f.readlines()
f.close()

profile_runs = [ 'for i, l in enumerate(input): d.dissociate(l, N=N)', 'for i in xrange(1000): d.associate()' ]

for p in profile_runs:
    print p
    profile.run(p)
    print "========================"
