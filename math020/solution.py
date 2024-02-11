"""Problem 20"""


def factorial(n):
    """function to find factorial of a number"""
    fact = str(n)
    remainder = 0
    for i in reversed(range(1, n)):
        new_num = ""
        for j in fact[::-1]:
            num = int(j)
            product = num * i + remainder
            if len(str(product)) == 1:
                new_num = str(product) + new_num
                remainder = 0
            else:
                new_num = str(product % 10) + new_num
                remainder = product // 10
        if remainder:
            new_num = str(remainder) + new_num
            remainder = 0
        fact = new_num
    return fact


def solver(n):
    """function to find sum of all digits of a factorial"""
    fact = factorial(n)
    ans = 0
    for i in fact:
        ans += int(i)
    return ans


def answer():
    """calling solver function from solver file"""
    return solver(100)


if __name__ == "__main__":
    print(answer())
    print(solver(150))
