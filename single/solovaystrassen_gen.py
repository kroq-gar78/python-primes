#!/usr/bin/env python

# Find all primes in the given range using the Solovay-Strassen Primality Test

import sys
from solovaystrassen import solovaystrassen
from writeresults import writeresults

args = xrange(int(sys.argv[1]),int(sys.argv[2])+1)

primesFound = 0

for num in args:
	if (solovaystrassen(num)):
		primesFound += 1

writeresults("solovaystrassen",int(sys.argv[2])-int(sys.argv[1])+1,int(primesFound))
