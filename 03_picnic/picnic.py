#!/usr/bin/env python3
"""A nice summer picnic"""

import argparse


def get_args():
    """Are you tired of arguments yet? Cause there'll be way more"""
    parser = argparse.ArgumentParser(
        description="What are we bringing, boss?",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "items", metavar="item", nargs="+", help="Thing(s) a picnic needs"
    )
    parser.add_argument("-s", "--sorted", help="Sort the list?", action="store_true")
    return parser.parse_args()


def main():
    """Make sure to bring the waterproof blanket"""
    args = get_args()
    comma_counter = 1

    if args.sorted:
        args.items.sort()

    if len(args.items) == 1:
        print(f"You are bringing {args.items[0]}.")
    elif len(args.items) == 2:
        print(f"You are bringing {args.items[0]} and {args.items[1]}.")
    elif len(args.items) > 2:
        for x in range(len(args.items) - 2):
            args.items.insert(comma_counter, ", ")
            comma_counter = comma_counter + 2
        args.items.insert(-1, ", and ")
        print(f"You are bringing {''.join(args.items)}.")


if __name__ == "__main__":
    main()
