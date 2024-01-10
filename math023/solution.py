"""Day-23"""


def is_abundant(num):
    """function to check if the number is abundant"""
    factors_sum = [i + num // i for i in range(2, int(num**0.5) + 1) if num % i == 0]
    ans = sum(factors_sum) + 1
    if int(num**0.5) == num**0.5:
        ans -= num**0.5
    return bool(num < ans < 28123)


def solver(p=None, q=None):
    """generalize function"""
    start, end = 1, p
    if q:
        start, end = p, q
    abundant_list = [x for x in range(start, end + 1) if is_abundant(x)]
    numbers_list = list(range(start, end + 1))
    sum_abundant_list = [
        abundant_list[i] + abundant_list[j]
        for i in range(0, len(abundant_list))
        for j in range(i, len(abundant_list))
    ]
    ans = set(numbers_list) - set(sum_abundant_list)
    return sum(ans)


def answer():
    """answer"""
    return solver(28123)


if __name__ == "__main__":
    print(answer())
    print(solver(100))
