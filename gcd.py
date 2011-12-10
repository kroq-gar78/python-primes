#!/usr/bin/python


def gcd(a,b):
	if( a==b or a==0 or b==0 ): return a|b
	if(a&1==0): # if 'a' even
		if(b&1==0): return (gcd(a>>1,b>>1)<<1)
		else: return gcd(a>>1,b)
	elif(b&1==0): return gcd(a,b>>1)
	else: # if 'a' and 'b' odd
		if(a>b): return gcd((a-b)>>1,b)
		else: return gcd((b-a)>>1,a)

if __name__ == "__main__":
	import sys
	print str(gcd(int(sys.argv[1]),int(sys.argv[2])))
