"""Problem 37"""


def is_truncatable(num, index):
    """return if the number is truncable or not"""
    if index == len(num):
        return True
    if is_prime(int(num[index:])) and is_prime(int(num[:-index])):
        return is_truncatable(num, index + 1)
    return False


def is_prime(num):
    """return if the number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solver():
    """return sum of Truncatable Primes"""
    ans = count = 0
    num = 23
    while count != 11:
        if is_prime(num) and is_truncatable(str(num), 1):
            ans += num
            count += 1
        num += 1
    return ans


if __name__ == "__main__":
    print(solver())
