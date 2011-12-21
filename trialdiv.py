#!/usr/bin/python

import math

# Trial Division primality test
# Manually checks all prime numbers against the input

def isPrime(n,primes=[2]):
	if(n&1==0): return (n==2)
	for i in primes:
		if(n%i==0): return False
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if n%i==0: return False
			if( not i in primes ): primes.append(i)
	
	#print primes
	
	for i in primes:
		if n%i == 0:
			return False
	return True

if __name__ == "__main__":
	import sys
	print isPrime(int(sys.argv[1])) 
