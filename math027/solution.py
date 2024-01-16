"""Day-27"""


def answer():
    """function to find product of the coefficients"""

    def is_prime(num):
        """function to check if number is prime or not"""
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    a, b, max_length = 0, 0, 0
    for i in range(-999, 1000):
        for j in range(-1000, 1001):
            count, n = 0, 0
            while True:
                num = (n * n) + (i * n) + (j)
                if is_prime(num):
                    count += 1
                    n += 1
                else:
                    break
            if max_length < count:
                max_length = count
                a, b = i, j
    return a * b


if __name__ == "__main__":
    print(answer())
