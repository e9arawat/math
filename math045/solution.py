"""Problem 45"""

import math


def solver():
    """return Triangular, Pentagonal, and Hexagonal"""
    hexagonal = [(n * (2 * n - 1)) for n in range(144, 100000)]
    for x in hexagonal:
        n = (1 + math.sqrt(1 + 24 * x)) / 6
        if n == int(n):
            return x
    return 0


if __name__ == "__main__":
    print(solver())
