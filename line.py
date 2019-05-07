#!/usr/bin/env python
import os
import glob
import argparse
import fnmatch

class LineCounter(object):

	def __init__(self, dir):
		# current location
		self.current_dir = dir

		# Core counters for the number of lines and files 
		self.line_count = 0
		self.file_count = 0


def main():
	__usage__ = "count the amount of lines and files under the current directory"
	parser = argparse.ArgumentParser(description=__usage__)
	group = parser.add_mutually_exclusive_group()
	parser.add_argument("x", help="base", type=int)
	parser.add_argument("y", help="exp", type=int)
	group.add_argument("-v", "--verbosity", action="store_true")
	group.add_argument("-q", "--quiet", action="store_true")
	args = parser.parse_args()
	ans = args.x * args.y
	if args.verbosity:
		print(f"{args.x} to the power of {args.y} equals {ans}")
	elif args.quiet:
		print(f"{args.x} * {args.y} == {ans}")
	else:
		print(ans)

if __name__ == '__main__':
	main()



