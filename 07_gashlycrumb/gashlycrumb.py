#!/usr/bin/env python3
"""Today we'll be dealing with morbid poetry"""

import argparse


def get_args():
    """pls gib args"""

    parser = argparse.ArgumentParser(
        description="Let's get some nice rhymes going",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "letter", metavar="letter", nargs="+", help="The alphabet is your buffet"
    )

    parser.add_argument(
        "-f",
        "--file",
        help="Alphabetized file",
        metavar="file",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
    )

    return parser.parse_args()


def main():
    """The only reason this is here is pylint"""
    args = get_args()
    letter_list = {}

    for line in args.file:
        letter_list[line[0].lower()] = line.rstrip()

    for letter in args.letter:
        print(letter_list.get(letter.lower(), f'I do not know "{letter}".'))


if __name__ == "__main__":
    main()
