#!/usr/bin/env python

from factorize import factorize
from pfactors import pfactors
import math

def totient(n,factors=[]):
	if factors == []:
		factors = pfactors(n)
	for i in factors:
		n = int(n*(1-1.0/i))
	return n
	
if __name__ == "__main__":
	import sys
	print totient(int(sys.argv[1]))
