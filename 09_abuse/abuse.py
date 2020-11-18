#!/usr/bin/env python3
"""
Author : Me
Date   : you wish
Purpose: Utter Chaos
"""
import random
import argparse


def get_args():
    """It's all downhill from here"""

    parser = argparse.ArgumentParser(
        description="Fresh insults right out of your terminal",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-a",
        "--adjectives",
        help="How many d'you want?",
        metavar="number",
        type=int,
        default=2,
    )

    parser.add_argument(
        "-n",
        "--number",
        help="The more the merrier!",
        metavar="insults",
        type=int,
        default=3,
    )

    parser.add_argument(
        "-s",
        "--seed",
        help="Let's see some seeds ;)",
        metavar="int",
        type=int,
        default=None,
    )

    args = parser.parse_args()
    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


def main():
    """Shh! This is a library!"""

    args = get_args()

    adjectives = """bankrupt base caterwauling corrupt
    cullionly detestable dishonest false filthsome filthy
    foolish foul gross heedless indistinguishable infected
    insatiate irksome lascivious lecherous loathsome
    lubbery old peevish rascaly rotten ruinous scurilous
    scurvy slanderous sodden-witted thin-faced toad-spotted
    unmannered vile wall-eyed""".split()

    nouns = """Judas Satan ape ass barbermonger beggar
    block boy braggart butt carbuncle coward coxcomb cur
    dandy degenerate fiend fishmonger fool gull harpy jack
    jolthead knave liar lunatic maw milksop minion
    ratcatcher recreant rogue scold slave swine traitor
    varlet villain worm""".split()

    random.seed(args.seed)

    for n in range(args.number):
        random_adj = random.sample(adjectives, args.adjectives)
        random_noun = random.choice(nouns)
        print(f'You {", ".join(random_adj)} {random_noun}!')


if __name__ == "__main__":
    main()
