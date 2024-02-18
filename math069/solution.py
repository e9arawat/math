""" 
Totient Maximum
"""


def answer():
    """
    Totient Maximum
    """
    all_primes = [
        x
        for x in range(1, 1000000)
        if all(x % i != 0 for i in range(2, int(x**0.5) + 1))
    ]
    max_totient = 1
    for prime in all_primes:
        max_totient *= prime
        if max_totient > 1000000:
            max_totient //= prime
            break
    return max_totient


if __name__ == "__main__":
    print(answer())
