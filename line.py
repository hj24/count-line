#!/usr/bin/env python
import os
import glob
import argparse
import fnmatch
from collections import defaultdict

class LineCounter(object):

	def __init__(self, dir):
		# current location
		self.current_dir = dir

		# Core counters for the number of lines and files 
		self.line_count = 0
		self.file_count = 0

		# sets to record the filter files suffix or specific files suffix
		self.select_suffix = set()
		self.filter_suffix = set()

		# dict for detail results, default count = 0
		self.final_files = defaultdict(int)

	def filter_mod(self, filter_list):
		print(filter_list)

	def specific_mod(self, suffix_list):
		print(suffix_list)

	def normal_mod(self):
		pass

	def show_results(self):
		print(f'file count: {self.file_count}')
		print(f'line count: {self.line_count}')

	def show_detail_results(self):
		pass

def main():
	__usage__ = "count the amount of lines and files under the current directory"
	parser = argparse.ArgumentParser(description=__usage__)

	group = parser.add_mutually_exclusive_group()
	group.add_argument("-s", "--suffix", type=str, 
						help="count by suffix file name, format: .suffix1.suffix2... e.g: .cpp.py (without space)")
	group.add_argument("-f", "--filter", type=str, 
						help="count without filter name, format: .suffix1.suffix2... e.g: .cpp.py (without space)")
	parser.add_argument("-d", "--detail", action="store_true",
						help="show detail results")
	
	args = parser.parse_args()

	current_dir = os.getcwd()
	counter = LineCounter(current_dir)

	if args.filter:
		args_list = args.filter.split('.')
		args_list.remove('')
		counter.filter_mod(args_list)
	elif args.suffix:
		args_list = args.suffix.split('.')
		args_list.remove('')
		counter.specific_mod(args_list)
	else:
		print(f'Search in {current_dir}' + f'{os.sep}')
		counter.normal_mod()

	if args.detail:
		counter.show_detail_results()
	else:
		counter.show_results()
		
if __name__ == '__main__':
	main()



