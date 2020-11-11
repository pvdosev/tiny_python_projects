#!/usr/bin/env python3
"""Informs users of things around the ship"""

import argparse


def get_arguments():
    """Fetch CLI arguments"""
    parser = argparse.ArgumentParser(
        description="Let's rock the boat",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "word", metavar="spotted", help="Yarr, what ye be seeing?"
    )

    return parser.parse_args()


def main():
    """Do the thing, Ju Li!"""

    args = get_arguments()

    if args.word[0].lower() in "aeiou":
        article = "an"
    else:
        article = "a"

    print("Ahoy, Captain, {} {} off the larboard bow!".format(article, args.word))


if __name__ == "__main__":
    main()
