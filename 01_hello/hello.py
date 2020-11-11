#!/usr/bin/env python3

import argparse


def argument_parse():
	"""Parse arguments *le gasp* """


	parser = argparse.ArgumentParser(description="come to the forbidden apple")
	parser.add_argument('-n', '--name', metavar='name', default='World', help="your own identifier")
	return parser.parse_args()

def main():
	"""This is where the magic happens"""


	args = argument_parse()
	print ("Hello, " + args.name + "!")


if __name__ == '__main__':
	main()