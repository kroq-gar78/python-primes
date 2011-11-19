#!/usr/bin/python

import sys
from trialdiv import isPrime
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if(isPrime(num)):
		primesFound += 1

writeresults("trialdiv",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
