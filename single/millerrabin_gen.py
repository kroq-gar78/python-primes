#!/usr/bin/python

import sys
from millerrabin import isPrime
from writeresults import writeresults

args = range(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if(isPrime(num)):
		primesFound += 1

writeresults("millerrabin",args[len(args)-1],int(primesFound))
