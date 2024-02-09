"""Problem 38"""


def solver():
    """return the largest Pandigital Multiples"""
    ans = 0
    test_list = [str(x) for x in range(1, 10)]
    for i in range(1, 9999):
        temp = ""
        for j in range(1, 9):
            temp += str(i * j)
            if len(temp) >= 9:
                break
        if len(temp) == 9 and sorted(temp) == test_list:
            ans = max(ans, int(temp))
    return ans


if __name__ == "__main__":
    print(solver())
