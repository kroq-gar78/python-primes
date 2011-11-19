#!/usr/bin/python

from expmod import expmod
import random
import sys

def isPrime(n,k=2,bases=[]):
	if(bases==[]): # if bases not given, use random 'a'
		for i in xrange(k):
			#print "Iteration " + str(i+1)
			a = random.randint(1,n-1)
			if expmod(a,n-1,n) != 1:
				return False
		return True
	else: # if bases given, use bases 'a' from the array
		print "Bases given"
		for a in bases:
			if (pow(a,n-1)-1)%n != 0:
				return False
		return True

if __name__ == "__main__":
	k=2 # default amount of iterations 
	if len(sys.argv) >= 3:
		k = int(sys.argv[2]) # times to repeat test
	n = int(sys.argv[1]) # number to test for primality
	#a = 78 # "Fermat witness" - test 'n' against this
	
	print isPrime(int(sys.argv[1]),k)
