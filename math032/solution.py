"""Day-32"""


def solver():
    """sum of all products whose multiplicand/multiplier/product"""
    digits = "123456789"
    result = set()
    for i in range(10):
        for j in range(1000, 10000):
            temp = str(i) + str(j) + str(i * j)
            if len(temp) == 9 and "".join(sorted(temp)) == digits:
                result.add(i * j)
            elif len(temp) > 9:
                break

    for i in range(10, 100):
        for j in range(100, 1000):
            temp = str(i) + str(j) + str(i * j)
            if len(temp) == 9 and "".join(sorted(temp)) == digits:
                result.add(i * j)
            elif len(temp) > 9:
                break

    return sum(result)


if __name__ == "__main__":
    print(solver())
