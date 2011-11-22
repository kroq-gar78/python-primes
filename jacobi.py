#!/usr/bin/python

from euclidean import gcd
import sys

def jacobi(n,m):
	if gcd(n,m) != 1: return jacobi(n/gcd(n,m),m/gcd(n,m))
	if n==1: return 1
	#print (n,m)
	if n&1==0:
		if m%8==3 or m%8==5: return (-1)*jacobi(n/2,m)
		else: return jacobi(n/2,m)
	if n>m: return jacobi(n%m,m)
	if n%4==3 and m%4==3: return (-1)*jacobi(m,n)
	else: return jacobi(m,n)

if __name__ == "__main__":
	print jacobi(int(sys.argv[1]),int(sys.argv[2]))
