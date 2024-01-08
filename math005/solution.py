"""Day-5 Math"""


def hcf(a, b):
    """function to find highest common factor"""
    if b == 0:
        return a
    return hcf(b, a % b)


def solver(p, q):
    """function to fine minimum number that is divisible by all number between p and q"""
    start, end = min(p, q), max(p, q)
    ans = start
    for i in range(start + 1, end + 1):
        ans = (i * ans) // (hcf(i, ans))
    return ans


def answer():
    """calling solver function"""
    return solver(1, 20)


if __name__ == "__main__":
    print(answer())
    print(solver(2, 10))
