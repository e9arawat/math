"""Problem 39"""


def is_property(p, i, j):
    """return if the property is satisfied or not"""
    if (p**2) // 2 == -(i * j - i * p - j * p):
        return True
    return False


def answer():
    """return the maximum number for which the number of solutions maximised"""
    ans = max_solution = 0
    for p in range(12, 1001):
        count = 0
        for i in range(1, p - 1):
            for j in range(i + 1, p):
                if is_property(p, i, j):
                    count += 1
        if count > max_solution:
            max_solution = count
            ans = p
    return ans


if __name__ == "__main__":
    print(answer())
