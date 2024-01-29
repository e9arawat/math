"""day-34"""


def find_factorial(num):
    """function to find factorial of a number"""
    fact = 1
    for i in range(2, num + 1):
        fact *= i

    return fact


def find_sum_factorial(num):
    """function to find summ of all the numbers"""
    temp = str(num)
    ans = 0
    for i in temp:
        ans += find_factorial(int(i))
    return ans == num


def solver():
    """function to find Digit Factorials"""
    ans = 0
    for i in range(3, 1000000):
        ans += i if find_sum_factorial(i) else 0
    return ans


if __name__ == "__main__":
    print(solver())
