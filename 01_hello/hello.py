#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="come to the forbidden apple")
parser.add_argument('-n', '--name', metavar='name', default='World', help="your own identifier")
args = parser.parse_args()

print ("Hello, " + args.name + "!")