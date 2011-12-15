#!/usr/bin/python

# A program that uses the Euclidean Algorithm for greatest common divisor
#
# Created by Aditya Vaidya kroq-gar78 <kroq.gar78@gmail.com>


def gcd(a,b):
	while b: a,b = b,a%b
	return a

if __name__ == "__main__":
	import sys
	print str(gcd(int(sys.argv[1]),int(sys.argv[2])))

