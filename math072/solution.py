""" 
Counting Fractions
"""


def find_relative_primes(num):
    """
    return the number of relative primes
    """
    result = num
    prime = 2
    while prime * prime <= num:
        if num % prime == 0:
            while num % prime == 0:
                num //= prime
            result -= result // prime
        prime += 1
    if num > 1:
        result -= result // num
    return result


def answer():
    """
    Counting Fractions
    """
    return sum(find_relative_primes(num) for num in range(2, 1000001))


if __name__ == "__main__":
    print(answer())
