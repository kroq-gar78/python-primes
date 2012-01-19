#!/usr/bin/python

import random
import time

def isPrime(n,k=2,bases=[],seed=time.time()):
	random.seed(time.time())
	s=0
	d=n-1
	while(d&1==0):
		d >>= 1
		s += 1
	if(bases==[]): # if bases not given, use random 'a'
		for i in xrange(k):
			nextLoop = False
			a = 0
			while(True): # generate 'a' that hasn't been used already
				a = random.randint(1,n-1)
				#print "New 'a'"
				if not (a in bases):
					break
			x = pow(a,d,n)
			if x==1 or x==n-1:
				continue
			for r in xrange(s):
				#x = pow(x,2)%n
				x = (x*x)%n
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
		basesTested = 0 # makes sure that all bases given are NOT larger than n-1
		for a in bases:
			if a > n-1:
				continue
			nextLoop = False
			x = pow(a,d,n)
			if x==1 or x==n-1:
				continue
			for r in xrange(s):
				#x = pow(x,2)%n
				x = (x*x)%n
				if x==1: #1^2 will always be 1, so it will never reach the next 'if' statement
					#print "Breakpoint 1", a
					return False
				if x==n-1:
					nextLoop = True
					break
			if( not nextLoop ):
				#print "Breakpoint 2", a
				return False
			basesTested = basesTested+1
			#else: continue
		if basesTested == 0: return "Bases too large for number to be tested."
		return True

if __name__ == "__main__":
	import sys
	k=2 # default amount of iterations
	if len(sys.argv) < 3:
			if len(sys.argv) == 1:
				print "ERROR: NEED AT LEAST 1 NUMERICAL ARGUMENT TO TEST PRIMALITY."
				exit()
	else:
		k = int(sys.argv[2]) # amount of bases to test against
	n = int(sys.argv[1]) # number to test for primality

	print isPrime(n,k)
