#!/usr/bin/python

# Lucas Primality Test
# http://en.wikipedia.org/wiki/Lucas_primality_test

from expmod import expmod
from gcd import gcd
#from pminus1 import factorize

def factors_of(n):
	    f = 2
	    for step in chain([0,1,2,2], cycle([4,2,4,2,4,6,2,6])):
	        f += step
	 
	        if f*f > n:
	            if n != 1:
	                yield n
	            break
	 
	        if n%f == 0:
	            yield f
	            while n%f == 0:
	                n /= f

def isPrime(n,k=2,bases=[]):
	if(n&1==0): return (n==2) 
	factors = list( factors_of(n))
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

if __name__ == "__main__":
	import sys
	print isPrime(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
