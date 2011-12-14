#!/usr/bin/python

import sys
from lucaslehmer import lucaslehmer
from trialdiv import isPrime
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if(lucaslehmer(num)):
		primesFound += 1
		print "M%d"%num,
		sys.stdout.flush()

writeresults("lucaslehmer",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))

