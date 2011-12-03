#!/usr/bin/python

from expmod import expmod
from jacobi import jacobi
import random
import sys

def isPrime(n,k=2,bases=[]):
	if(n==2): return True
	if(n&1==0): return False
	if(bases==[]): # if bases not given, use random 'a'
		for i in range(k):
			a = 0
			while(True): # generate 'a' that hasn't been used already
				a = random.randint(1,n-1)
				print "New 'a'"
				if not (a in bases):
					break
			#print a
			x=jacobi(a,n)%n
			if x==0 or expmod(a,(n-1)/2,n) != x:
				return False
		return True
	else: # if bases given, use bases 'a' from the array
		basesTested = 0 # makes sure that all bases given are NOT larger than n-1
		for a in bases:
			if a > n-1:
				continue
			x=jacobi(a,n)
			if x==0 or expmod(a,(n-1)/2,n) != x:
				return False
			basesTested = basesTested+1
		if basesTested == 0: return "Bases too large for number to be tested."
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

	print isPrime(n,k)
