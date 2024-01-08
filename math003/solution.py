"""Day-3"""
import math


def is_prime(num):
    """function to find if number is prime or not"""
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solver(value):
    """solver function"""
    prime_list = []
    result = 0
    square_root_of_n = int(value ** (0.5))
    for i in range(2, square_root_of_n + 1):
        if value % i == 0:
            mirror = value // i
            if is_prime(mirror):
                return mirror
            if is_prime(i):
                prime_list.insert(0, i)

    if len(prime_list) == 0:
        result = value
    else:
        result = prime_list[0]
    return result


def answer():
    """calling solver function"""
    return solver(600851475143)


def main():
    print(answer())
    print(solver(23445656))


main()
