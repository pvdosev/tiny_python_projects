#!/usr/bin/env python3
"""Why are we here? Just to suffer?"""

import argparse
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("text", metavar="text", help="Shout, shout, let it all out!")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Do you want it written down?",
        metavar="str",
        type=str,
        default="",
    )

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()
    lower = ""

    if os.path.isfile(args.text):
        lower = open(args.text).read().rstrip()
    else:
        lower = args.text

    upper = lower.upper()

    if args.outfile:
        out_file = open(args.outfile, "wt")
        out_file.write(f"{upper}\n")
    else:
        print(upper)


if __name__ == "__main__":
    main()
