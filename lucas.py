#!/usr/bin/python

# Lucas Primality Test
# http://en.wikipedia.org/wiki/Lucas_primality_test

from expmod import expmod
from gcd import gcd
from pminus1 import factorize
import sys

def isPrime(n,k=2,bases=[]):
	if(n==2): return True
	if(n&1==0): return False # if even, not prime
	factors=factorize(n)
	if(bases==[]): # if bases not given, use random 'a'
		for i in xrange(k):
			#print "Iteration " + str(i+1)
			a = 0
			while(True): # generate 'a' that hasn't been used already
				a = random.randint(1,n-1)
				print "New 'a'"
				if not (a in bases):
					break
			if expmod(a,n-1,n) != 1:
				return False
			for j in factors
		return True
	else: # if bases given, use bases 'a' from the array
		print "Bases given"
		basesTested = 0 # makes sure that all bases given are NOT larger than n-1
		for a in bases:
			if a > n-1:
				continue
			if expmod(a,n-1,n) != 1:
				return False
			basesTested = basesTested+1
		if basesTested == 0: return "Bases too large for number to be tested."
		return True

if __name__ == "__main__":
	print isPrime(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
