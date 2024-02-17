"""
Combinatoric Selections
"""


def fact(num):
    """
    return the factorial of a number
    """
    if num < 1:
        return 1
    return num * fact(num - 1)


def combination(n, r):
    """
    return combination of that number
    """
    return (fact(n)) / (fact(r) * fact(n - r))


def answer():
    """
    Combinatoric Selections
    """
    count = 0
    for n in range(101):
        for r in range(101):
            if combination(n, r) > 1000000:
                count += 1
    return count


if __name__ == "__main__":
    print(answer())
