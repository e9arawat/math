"""Day-4 math"""


def is_palindrome(n):
    """function to check is n is palindrome"""
    temp, i = str(n), 0
    j = len(temp) - 1
    while i < j:
        if temp[i] != temp[j]:
            return False
        i, j = i + 1, j - 1
    return True


def solver(n, p=None, q=None):
    """function to find largest palindrome"""
    result = 0
    start, end = 10 ** (n - 1), (10**n)
    if p and q:
        start, end = p, q + 1
    elif p:
        end = p
    for i in reversed(range(start, end)):
        for j in reversed(range(start, (i + 1))):
            if is_palindrome(i * j):
                result = max(result, (i * j))
                break
    return result


def answer():
    """calling solver function"""
    return solver(2)


if __name__ == "__main__":
    print(answer())
    print(solver(3, 10, 81))
