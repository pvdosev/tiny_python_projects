#!/usr/bin/env python3
"""Awwwh, my own lil' CLI util!!"""

import argparse
import sys

def get_args():
    """Arrr, yet more arrrgs"""
    parser = argparse.ArgumentParser(
        description='Will Crusher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        help='A file that counts!',
                        nargs='*',
                        metavar='file',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()

def main():
    """Water closet, wand curse, woozy client"""

    args = get_args()
    total_lines = 0
    total_words = 0
    total_bytes = 0

    """Check for args.file, otherwise use stdin. Turn the counting into a function?"""

    for fh in args.file:
        current_lines = 0
        current_words = 0
        current_bytes = 0
        for line in fh:
            current_lines += 1
            current_words += len(line.split())
            current_bytes += len(line)
        total_lines += current_lines
        total_words += current_words
        total_bytes += current_bytes

        print(f"{current_lines:8}{current_words:8}{current_bytes:8} {fh.name}")
    if len(args.file) > 1:
        print(f"{total_lines:8}{total_words:8}{total_bytes:8} total")


if __name__ == '__main__':
    main()