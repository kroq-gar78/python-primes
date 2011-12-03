#!/usr/bin/python

def expmod(a,b,c):
	result = 1
	while b>0:
		if(b&1==1): result = (result*a)%c
		b>>=1
		a=(a*a)%c # use mulmod here?
	return result
	
if __name__ == "__main__":
	print expmod(int(sys.argv[1]),int(sys.argv[2]),int(argv[3]))
