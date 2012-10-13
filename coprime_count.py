#!/usr/bin/env python

from factorize import factorize
from pfactors import pfactors
import math

def coprime_count(n,factors=[],primes=[2]):
	if factors == []:
		factors = factorize(n,primes=primes)
	for i in factors.iterkeys():
		n = int(n*(1-1.0/i))
	return n
	
if __name__ == "__main__":
	import sys
	print coprime_count(int(sys.argv[1]))
