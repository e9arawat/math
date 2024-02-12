"""Problem 46"""

import math


def is_property(num, smaller_primes):
    """return if the number satisfy the property or not"""
    for p in smaller_primes:
        temp = math.sqrt((num - p) / 2)
        if round(temp) == temp:
            return True
    return False


def answer():
    """Goldbach's Other Conjecture"""
    all_primes = [
        x
        for x in range(2, 100000)
        if all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    ]
    for i in range(3, 10000, 2):
        if i in all_primes:
            continue
        smaller_primes = [x for x in all_primes if x < i]
        if not is_property(i, smaller_primes):
            return i
    return 0


if __name__ == "__main__":
    print(answer())
