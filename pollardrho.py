#!/usr/bin/python

# Pollard's Rho Algorithm

from gcd import gcd
from mulmod import mulmod
import random
import sys

def factorize(n):
	 
		
def findfactor(n):
	if n&1==0: return 2
	y,c,m = random.randint(1,n-1),random.randint(1,n-1),random.randint(1,n-1)
	g,r,q=1,1,1
	while g==1:
		x=y
		for i in xrange(r):
			y = (mulmod(y,y,n)+c)%n
		
		k=0
		while (k<r and g==1):
			ys = y
			for i in xrange(min(m,r-k)):
				y = (mulmod(y,y,n)+c)%n
				q = q*(abs(x-y))%n
			g=gcd(q,n)
			k=k+m
		r<<=1
	if g==n:
		while True:
			ys = (mulmod(ys,ys,n)+c)%n
			g = gcd(abs(x-ys),n)
			if g>1:
				break
	
	return g
	
