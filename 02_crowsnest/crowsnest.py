#!/usr/bin/env python3
"""Informs users of things around the ship"""

import argparse

def get_arguments():
	parser = argparse.ArgumentParser(
		description = "Let's rock the boat",
		formatter_class = argparse.ArgumentDefaultsHelpFormatter
		)

	parser.add_argument('positional',
		metavar="spotted",
		help="Yarr, what ye be seeing?")

	return parser.parse_args()

def main():
	args = get_arguments()
	print("Ahoy, Captain, a " + args.positional + " off the larboard bow!")

if __name__ == '__main__':
	main()
