#!/usr/bin/python

from jacobi import jacobi
import random
import sys

def isPrime(n,k=2,bases=[]):
	if(bases==[]): # if bases not given, use random 'a'
		for i in range(k):
			a = random.randint(2,n-1)
			x=jacobi(a,n)
			if x==0 or (a**((n-1)/2))%n != x:
				return False
		return True
	else: # if bases given, use bases 'a' from the array
		for a in bases:
			x=jacobi(a,n)
			if x==0 or (a**((n-1)/2))%n != x:
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

	print isPrime(n,k)
