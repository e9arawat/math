""" Problem 44"""


def solver():
    """return the pair"""
    pentagon = [(n * (3 * n - 1)) // 2 for n in range(1000, 2400)]
    for index, x in enumerate(pentagon):
        a = x
        for i in pentagon[:index]:
            if a - i in pentagon and a + i in pentagon:
                return a - i
    return 0

if __name__ == "__main__":
    print(solver())
