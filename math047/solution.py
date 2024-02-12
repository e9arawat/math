"""Problem 47"""


def is_prime(num):
    """return if the number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_factors(num):
    """return the factors of a number"""
    factors = 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            if is_prime(i):
                factors += 1
            if is_prime(num // i):
                factors += 1
    return factors


def answer():
    """Distinct Primes Factors"""
    num_factors_dict = {}
    for num in range(100000, 150000):
        factors = find_factors(num)
        if factors == 4:
            num_factors_dict[num] = factors

    for key in num_factors_dict:
        if (
            key + 1 in num_factors_dict
            and key + 2 in num_factors_dict
            and key + 3 in num_factors_dict
        ):
            return key
    return 0


if __name__ == "__main__":
    print(answer())
