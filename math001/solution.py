"""Day-1"""


def answer():
    """answer"""
    r = 1000
    nums = set()
    for i in range(1, (r // 3) + 1):
        if (i * 3) < r:
            nums.add(i * 3)
        if (i * 5) < r:
            nums.add(i * 5)
    return sum(nums)


def solver(factors, start, end):
    """solver"""
    a = min(factors)
    nums = set()
    for i in range(1, (end // a) + 1):
        for j in factors:
            if (j * i) >= start and (j * i) <= end:
                nums.add(j * i)
    return sum(nums)


if __name__ == "__main__":
    print(answer())
    print(solver([2, 3, 5, 7, 11], 34567, 1234567))
