#!/usr/bin/env python

import math

def highest_prime_factor2(n):
	if isprime(n):
		return n
	for x in xrange(2,int(n ** 0.5 + 1)):
		if not n % x:
			return highest_prime_factor2(n/x)
			
def isprime(n):
	for x in xrange(2,int(n ** 0.5 + 1)):
		if not n % x:
			return False
	return True

def highest_prime_factor(n,primes=[2]):
	#results = isPrime(n,primes)
	#if results[0]: return n
	for i in primes:
		while( n%i==0 ):
			ndivi = n/i
			if ndivi>1:
				n=ndivi
			else:
				return n
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime=True
		for j in primes:
			if(i%j==0): ifprime=False; break
		if ifprime:
			while( n%i==0 ):
				ndivi = n/i
				if ndivi>1:
					n=ndivi
				else:
					return n
				print n
	return n
	
def isPrime(n,primes=[2]):
	if(n&1==0): return [n==2,primes]
	for i in primes:
		if(n%i==0): return [False,primes]
	for i in xrange(primes[len(primes)-1],int(math.sqrt(n))+1):
		ifprime = True
		for j in primes:
			if i%j == 0:
				ifprime = False
				break
		if ifprime:
			if n%i==0: return [False,primes]
			if( not i in primes ): primes.append(i)
	
	#print primes
	
	for i in primes:
		if n%i == 0:
			return [False,primes]
	return [True,primes]

if __name__ == "__main__":
	import sys
	print highest_prime_factor(int(sys.argv[1])) 
