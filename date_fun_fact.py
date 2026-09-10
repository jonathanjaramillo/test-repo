#!/usr/bin/env python3
"""Print today's date and a random fun fact."""

import random
from datetime import date

FUN_FACTS = [
    "Honey never spoils; edible pots have been found in ancient Egyptian tombs.",
    "Octopuses have three hearts and blue blood.",
    "Bananas are berries, but strawberries are not.",
    "A day on Venus is longer than its year.",
    "Wombat poop is cube-shaped.",
    "The Eiffel Tower can grow more than 15 cm taller in summer heat.",
    "Sharks existed before trees did.",
    "There are more possible chess games than atoms in the observable universe.",
]


def main():
    print(f"Today's date: {date.today():%A, %B %d, %Y}")
    print(f"Fun fact: {random.choice(FUN_FACTS)}")


if __name__ == "__main__":
    main()
