#!/usr/bin/python

# A program that uses the Euclidean Algorithm for greatest common divisor

# Created by Aditya Vaidya kroq-gar78 <kroq.gar78@gmail.com>


def gcd(a,b):
	val1=a
	val2=b
	while val2>0:
		remainder = val1%val2
		val1,val2 = val2,remainder
	return val1

if __name__ == "__main__":
	import sys
	print str(gcd(int(sys.argv[1]),int(sys.argv[2])))

