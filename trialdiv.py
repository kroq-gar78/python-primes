#!/usr/bin/python

import math
import sys

def isPrime(n):
	if(n==2): return True
	primes = [2]
	for i in range(2,int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			primes.append(i)
	
	#print primes
	
	for i in primes:
		if n%i == 0:
			return False
	return True

if __name__ == "__main__":
	print( isPrime(int(sys.argv[1])) )
