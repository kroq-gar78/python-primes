#!/usr/bin/env python

# Find all primes in the given range using Fermat's Primality Test

import sys
from fermat import fermat
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if(fermat(num)):
		primesFound += 1

writeresults("fermat",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
