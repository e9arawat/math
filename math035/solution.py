"""Day-35"""


def is_circular_prime(num):
    """function to find if number is circular prime"""
    temp = str(num)
    for i in range(1, len(temp)):
        temp_num = temp[i:] + temp[:i]
        if not is_prime(int(temp_num)):
            return False
    return True


def is_prime(num):
    """function to find if number is prime"""
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solver(p, q=None):
    """function to find Circular Primes"""
    start, end = 2, p
    if q:
        start, end = p, q
    ans = 0
    for i in range(start, end + 1):
        if is_prime(i) and is_circular_prime(i):
            ans += 1
    return ans


def answer():
    """calling solver function"""
    return solver(1000000)


if __name__ == "__main__":
    print(answer())
    print(solver(10, 100))
