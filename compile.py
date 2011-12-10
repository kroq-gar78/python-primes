#!/usr/bin/python

import py_compile
import sys

if __name__ == "__main__":
	py_compile.compile(str(sys.argv[1]))
