"""Problem 50"""


def is_prime(num):
    """return if the number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def answer(n):
    """return the Consecutive Prime Sum"""
    all_primes = []
    num = 2
    while sum(all_primes) < n:
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            all_primes.append(num)
        num += 1
    max_primes = []
    l = j = len(all_primes)
    while j != 0:
        i = 0
        while i + j < l + 1:
            current_primes = all_primes[i : i + j]
            if (
                sum(current_primes) <= n
                and is_prime(sum(current_primes))
                and len(current_primes) > len(max_primes)
            ):
                max_primes = current_primes
            i = i + 1
        j = j - 1
    return sum(max_primes)


if __name__ == "__main__":
    print(answer(1000000))
