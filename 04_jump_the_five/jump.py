#!/usr/bin/env python3
"""This is based off of some popular crime show, I hear"""

import argparse


def get_args():
    """Argumentation documentation"""
    parser = argparse.ArgumentParser(
        description="Ayy, I'm typin' heah!",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "string", metavar="string", help="Hey kid, wanna scramble some numbers?"
    )

    return parser.parse_args()


def main():
    """Don't mind me, just moving around some numbers"""
    args = get_args()
    scrambled = ""
    number_dict = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    for char in args.string:
        scrambled += number_dict.get(char, char)

    print(scrambled)


if __name__ == "__main__":
    main()
