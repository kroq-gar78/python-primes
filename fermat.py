#!/usr/bin/python

from expmod import expmod
import random

def isPrime(n,k=2,bases=[]):
	if(n&1==0): return (n==2)
	elif(n%5==0): return (n==5)
	if(bases==[]): # if bases not given, use random 'a'
		for i in xrange(k):
			#print "Iteration " + str(i+1)
			a = 0
			while(True): # generate 'a' that hasn't been used already
				a = random.randint(1,n-1)
				#print "New 'a'"
				if not (a in bases):
					break
			if expmod(a,n-1,n) != 1:
				return False
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
	import sys
	k=2 # default amount of iterations 
	if len(sys.argv) >= 3:
		k = int(sys.argv[2]) # times to repeat test
	n = int(sys.argv[1]) # number to test for primality
	#a = 78 # "Fermat witness" - test 'n' against this
	
	print isPrime(int(sys.argv[1]),k)
