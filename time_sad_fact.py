#!/usr/bin/env python3
"""Print the current time of day and a random sad fact."""

import random
from datetime import datetime

SAD_FACTS = [
    "The last male northern white rhino died in 2018, leaving the subspecies functionally extinct.",
    "Loneliness is estimated to be as harmful to health as smoking 15 cigarettes a day.",
    "Around one in three of all food produced for humans is wasted while millions go hungry.",
    "The Lonesome George tortoise died in 2012 as the last of his species.",
    "Sea turtles often eat plastic bags because they look like jellyfish.",
    "More than half of the world's coral reefs have been lost since the 1950s.",
    "Many people's last text messages go unanswered simply because the other person got busy.",
]


def main():
    print(f"Current time: {datetime.now():%I:%M %p}")
    print(f"Sad fact: {random.choice(SAD_FACTS)}")


if __name__ == "__main__":
    main()
