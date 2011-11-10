#!/usr/bin/python

import random
import sys

def isPrime(n,k):
	
	if( n == 2 ):
		return True
	
	s=0
	d=n-1
	while(d%2==0):
		d >>= 1
		s += 1
	
	nextLoop = False
	
	for i in xrange(k):
		a = i+2
		x = pow(a,d)%n
		if x==1 or x==n-1:
			nextLoop = True
		for r in xrange(s-1):
			x = pow(x,2)%n
			if x==1: #1^2 will always be 1, so it will never reach the next if statement
				return False
			if x==n-1:
				nextLoop = True
		if( not nextLoop ):
			return False
	return True

if __name__ == "__main__":
	if len(sys.argv) < 3:
		if len(sys.argv) == 2:
			print "WARNING: RECCOMENDED TO INPUT PREFERRED ACCURACY."
			k = 2
		else:
			print "ERROR: NEED AT LEAST 1 NUMERICAL ARGUMENT TO TEST PRIMALITY."
			exit()
	else:
		k = int(sys.argv[2]) # accuracy of the test
	n = int(sys.argv[1]) # number to test for primality

	print ifprime(n,k)
