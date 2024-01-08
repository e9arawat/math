"""Amicable Numbers"""


def factors_sum(n):
    """function to find sum of factors"""
    sum_of_factors = 0
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            sum_of_factors = sum_of_factors + x + n // x
    return sum_of_factors + 1


def solver(p: int = None, q: int = None):
    """function to find sum of amicable numbers"""
    start, end = 1, p
    if q:
        start, end = p, q
    num_fact_pair = {}
    ans = 0
    for num in range(start, end + 1):
        sum_of_factors = factors_sum(num)
        if sum_of_factors in num_fact_pair and num_fact_pair[sum_of_factors] == num:
            ans = ans + num + sum_of_factors
        num_fact_pair[num] = sum_of_factors
    return ans


def answer():
    """calling solver function"""
    return solver(1, 9999)


if __name__ == "__main__":
    print(answer())
    print(solver(1, 284))
