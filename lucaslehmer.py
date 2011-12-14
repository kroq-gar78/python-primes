#!/usr/bin/env python

# Lucas-Lehmer Primality Test for Mersenne Numbers

from trialdiv import isPrime

def lucaslehmer(p):
	if( not isPrime(p) ): return False # p must be prime
	s = 4
	m = (1<<p)-1
	for i in xrange(3,p+1):
		s = ((s*s)-2)%m
	return s==0

if __name__ == "__main__":
	import sys
	print lucaslehmer(int(sys.argv[1]))
