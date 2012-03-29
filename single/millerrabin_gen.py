#!/usr/bin/python

# Find all primes in the given range using the Miller-Rabin Primality Test

import sys
from millerrabin import isPrime
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if(isPrime(num)):
		primesFound += 1

writeresults("millerrabin",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
