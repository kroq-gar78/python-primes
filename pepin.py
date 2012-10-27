#!/usr/bin/env python

# Pepin's Primality Test for Fermat numbers
# Created by Aditya Vaidya <kroq.gar78@gmail.com>

def pepin(n):
	if n==3: return True
	return pow(3,(n-1)>>1,n)==n-1
	
# pepin(n), except by passing the index of Fermat number (index startign with 0)
def pepin_term(n):
	from fermat_num import fermat_num
	return pepin(fermat_num(n))


if __name__ == "__main__":
	import sys
	print pepin(int(sys.argv[1]))
