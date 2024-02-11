"""Day-24"""

import math


def factorial(num):
    """function to find factorial of a number"""
    return math.prod(list(range(2, num + 1)))


def solver(input_string: str, term: int):
    """function to find nth lexographical combination"""
    input_string, ans, n = sorted(input_string), "", len(input_string) - 1
    while n:
        fact = factorial(n)
        quotient = math.ceil(term / fact)
        term = term % fact or fact
        ans += input_string[quotient - 1]
        input_string.pop(quotient - 1)
        n -= 1
        if term == 1:
            break
    return ans + "".join(input_string)


def answer():
    """calling solver function"""
    return solver("0213456789", 1000000)


if __name__ == "__main__":
    print(answer())
    print(solver("01234a", 2))
