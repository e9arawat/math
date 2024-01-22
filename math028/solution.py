"""Day-28"""


def solver(n):
    """function to find sum of diagonals"""
    if n == 0:
        return 0
    i, ans, result = 1, 0, 0

    if n % 2 != 0:
        i, ans, result = 2, 1, 1

    while i < n:
        for _ in range(4):
            ans += i
            result += ans
        i += 2
    return result


def answer():
    """calling solver function"""
    return solver(1001)


if __name__ == "__main__":
    print(answer())
    print(solver(5))
