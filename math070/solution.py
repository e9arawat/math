""" 
Totient Permutation
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
    Totient Permutation
    """
    min_totient = 10000000
    min_totient_num = 0
    for i in range(2, 10000000):
        relative_primes = find_relative_primes(i)
        if (
            sorted(str(i)) == sorted(str(relative_primes))
            and min_totient > i / relative_primes
        ):
            min_totient = i / relative_primes
            min_totient_num = i
    return min_totient_num


if __name__ == "__main__":
    print(answer())
