"""
Spiral Primes
"""


def is_prime(num):
    """
    return is the number is prime or not
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer():
    """
    Spiral Primes
    """
    dif = 2
    diagonal_elements = 1
    primes = 0
    num = 1
    while True:
        for _ in range(4):
            num += dif
            if is_prime(num):
                primes += 1
        diagonal_elements += 4
        if float(primes / diagonal_elements) < 0.1:
            return dif + 1
        dif += 2


if __name__ == "__main__":
    print(answer())
