""" Problem 44"""

import math


def is_pentagon(num):
    """return if the number is pentagon or not"""
    n = (1 + math.sqrt(1 + 24 * num)) / 6
    if n == int(n):
        return True
    return False


def answer():
    """return the pair"""
    pentagon = [(n * (3 * n - 1)) // 2 for n in range(1000, 3000)]
    for index, x in enumerate(pentagon):
        a = x
        for i in pentagon[:index]:
            if is_pentagon(a - i) and is_pentagon(a + i):
                return a - i
    return 0


if __name__ == "__main__":
    print(answer())
