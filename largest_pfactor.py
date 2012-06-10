#!/usr/bin/env python

import sys

def highest_prime_factor(n):
   if isprime(n):
      return n
   for x in xrange(2,int(n ** 0.5) + 1):
      if not n % x:
         return highest_prime_factor(n/x)

def isprime(n):
   for x in xrange(2,int(n ** 0.5) + 1):
      if not n % x:
         return False
   return True

if  __name__ == "__main__":
   print highest_prime_factor(int(sys.argv[1]))
