#!/usr/bin/env python

import math
from factors_count import tau

def factors_product(n):
	return int(n**(tau(n)/2))
	
if __name__ == "__main__":
	import sys
	print factors_product(int(sys.argv[1]))
