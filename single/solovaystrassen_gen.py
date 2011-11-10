#!/usr/bin/python

import sys
from euclidean import gcd
from jacobi import jacobi
from solovaystrassen import isPrime
from writeresults import writeresults

args = range(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if (isPrime(num,bases=[2,3])):
		primesFound += 1

writeresults("solovaystrassen",args[len(args)-1],int(primesFound))
