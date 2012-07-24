#!/usr/bin/env python

# Find all primes in the given range using trial division

import sys
from trialdiv import trialdiv
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if(trialdiv(num)):
		primesFound += 1

writeresults("trialdiv",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
