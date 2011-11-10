#!/usr/bin/python

from euclidean import gcd

def jacobi(n,m):
	gcdVal = gcd(n,m)
	if( gcdVal != 1 ):
		return 0
	if( gcdVal == 1 ):
		return +- 1
	if n == 1:
		return 1
	if n%2 == 0:
		if m%8 == 3 or m%8 ==5:
			return (-1)*jacobi(n/2,m)
		return jacobi(n/2,m)
	if( n>m ):
		return jacobi(n%m,m)
	if( n%4==3 and m%4 ==3 ):
		return (-1)*jacobi(m,n)
	else:
		return jacobi(m,n)

if __name__ == "__main__":
	print jacobi(1001,9907)
