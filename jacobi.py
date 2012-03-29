#!/usr/bin/python

# Program to calculate the Jacobi symbol

from euclidean import gcd

def jacobi(n,m):
	gcdnm = gcd(n,m)
	if gcdnm != 1:
		#return jacobi(n/gcdnm,m/gcdnm)
		return 0
	if n==1: return 1
	if n&1==0:
		if m%8==3 or m%8==5: return (-1)*jacobi(n>>1,m)
		else: return jacobi(n>>1,m)
	if n>m: return jacobi(n%m,m)
	if n%4==3 and m%4==3: return (-1)*jacobi(m,n)
	else: return jacobi(m,n)

if __name__ == "__main__":
	import sys
	print jacobi(int(sys.argv[1]),int(sys.argv[2]))
