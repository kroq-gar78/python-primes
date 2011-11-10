#!/usr/bin/python

import random
import sys

def isPrime(n,k=2):
	
	if( n == 2 ):
		return True
	
	s=0
	d=n-1
	while(d&1==0):
		d >>= 1
		s += 1
	
	#bases = [2,3]
	
	#for a in bases:
	for a in xrange(k):
		nextLoop = False
		#a = i+2 #WTH?????
		a = random.randint(2,n-1)
		x = pow(a,d)%n
		if x==1 or x==n-1:
			continue
		for r in xrange(s):
			x = pow(x,2)%n
			if x==1: #1^2 will always be 1, so it will never reach the next 'if' statement
				#print "Breakpoint 1", a
				return False
			if x==n-1:
				nextLoop = True
				break
		if( not nextLoop ):
			#print "Breakpoint 2", a
			return False
		#else: continue
	return True

if __name__ == "__main__":
	if len(sys.argv) < 3:
		if len(sys.argv) == 2:
			print "WARNING: RECCOMENDED TO INPUT PREFERRED ACCURACY."
			#k = 2
		else:
			print "ERROR: NEED AT LEAST 1 NUMERICAL ARGUMENT TO TEST PRIMALITY."
			exit()
	else:
		k = int(sys.argv[2]) # accuracy of the test
	n = int(sys.argv[1]) # number to test for primality

	print isPrime(n,k)
