#!/usr/bin/python

import math

def isPrime(n):
	if(n&1==0): return (n==2)
	primes = [2]
	for i in range(2,int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if n%i==0: return False
			primes.append(i)
	
	#print primes
	
	for i in primes:
		if n%i == 0:
			return False
	return True

if __name__ == "__main__":
	import sys
	print isPrime(int(sys.argv[1])) 
