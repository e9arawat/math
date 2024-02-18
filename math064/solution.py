""" 
Odd Period Square Roots
"""

import math


def period_length(n):
    """
    return the length of the period
    """
    x = int(math.isqrt(n))
    y = x
    z = 1
    period = 0

    while True:
        y = ((x + y) // z) * z - y
        z = (n - y * y) // z
        period += 1
        if z <= 1:
            break

    return period


def answer():
    """
    Odd Period Square Roots
    """
    result = [
        period_length(n) % 2 != 0
        for n in range(1, 10001)
        if not math.isqrt(n) ** 2 == n
    ]

    return sum(result)


if __name__ == "__main__":
    print(answer())
