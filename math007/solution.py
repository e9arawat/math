"""Day-7"""


def nth_prime(prime_list, n):
    """function to find nth prime"""
    count, i = 0, 0
    while count < n:
        if prime_list[i] == 1:
            count += 1
        i += 1
    return i - 1


def all_primes(n):
    """function to find list of all prime numbers till n"""
    prime_list = [1] * n
    prime_list[0], prime_list[1] = 0, 0
    for i in range(2, int(n**0.5) + 1):
        if prime_list[i] == 1:
            for j in range(i, n):
                if i * j < n:
                    prime_list[i * j] = 0
                else:
                    break
    return prime_list


def solver(n: int):
    """main function"""
    size_iterator = 2
    total_prime = 0
    prime_list = []
    while total_prime < n:
        prime_list = all_primes(n * size_iterator)
        total_prime = sum(prime_list)
        size_iterator += 1
    ans = nth_prime(prime_list, n)
    return ans


def answer():
    """calling solver function"""
    return solver(10001)


if __name__ == "__main__":
    print(answer())
    print(solver(2000))
