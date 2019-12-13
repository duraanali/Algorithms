#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    pos = [['rock'], ['paper'], ['scissors']]

    def rounds(outcomes, a):
        if a == 0:
            return [[]]
        else:
            outcomes = rounds(outcomes, a - 1)
            print("outcomes", outcomes)
            new_outcomes = []
            print("new_outcomes", new_outcomes)
            for p in pos:
                for o in outcomes:
                    new_outcomes.append(p + o)
        return new_outcomes
    return rounds([], n)


print(rock_paper_scissors(2))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
