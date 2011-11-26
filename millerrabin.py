#!/usr/bin/python

from expmod import expmod
import random
import sys

def isPrime(n,k=2,bases=[]):
	if( n == 2 ): return True
	if( n&1==0 ): return False # if odd, not prime
	s=0
	d=n-1
	while(d&1==0):
		d >>= 1
		s += 1
	if(bases==[]): # if bases not given, use random 'a'
		for i in xrange(k):
			nextLoop = False
			a = random.randint(1,n-1)
			x = expmod(a,d,n)
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
	else: # if bases given, use bases 'a' from the array
		for a in bases:
			nextLoop = False
			x = expmod(a,d,n)
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
	k=2
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
