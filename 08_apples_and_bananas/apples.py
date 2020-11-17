#!/usr/bin/env python3
"""
Shoop da whoop!
"""

import argparse
import os


def get_args():
    """Gte cmomnda-lnei amguntsre"""

    parser = argparse.ArgumentParser(
        description="Let's change some vowels",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("input", metavar="str", help="Text or a file")

    parser.add_argument(
        "-v",
        "--vowel",
        help="What vowel to swap to",
        metavar="str",
        type=str,
        default="a",
        choices=["a", "e", "i", "o", "u"],
    )

    return parser.parse_args()


def main():
    """Make a blues noise here"""

    args = get_args()

    if os.path.isfile(args.input):
        text = open(args.input).read().rstrip()
    else:
        text = args.input

    print(
        text.translate(
            str.maketrans("aeiouAEIOU", 5 * args.vowel + 5 * args.vowel.upper())
        )
    )


if __name__ == "__main__":
    main()
