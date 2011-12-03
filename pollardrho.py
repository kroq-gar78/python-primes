#!/usr/bin/python

# Pollard's Rho Algorithm

from gcd import gcd
from mulmod import mulmod
import random
import sys

def factorize(n):
	 
		
def findfactor(n):
	if n&1==0: return 2
	x=random.randint(1,n-1)
	y=x
	c=random.randint(1,n-1)
	g=1
	while g==1:
		x = (mulmod(x,x,n)+c)%n
		y = (mulmod(y,y,n)+c)%n
		y = (mulmod(y,y,n)+c)%n
		g = gcd(abs(x-y),n)
