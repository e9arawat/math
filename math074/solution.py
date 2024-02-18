""" 
Digit Factorial Chains
"""


def factorial(num):
    """
    return the factorial of a number
    """
    if num < 2:
        return 1
    return num * factorial(num - 1)


def digits_factorial(num):
    """
    return the sum of factorial of digits
    """
    return sum(factorial(int(i)) for i in num)


def is_property(num):
    """
    return if the number satisfy the property or not
    """
    chain = [num]
    while True:
        next_num = digits_factorial(str(num))
        if next_num in chain:
            break
        chain.append(next_num)
        num = next_num
    if len(chain) == 60:
        return True
    return False


def answer():
    """
    Digit Factorial Chains
    """
    count = 0
    for num in range(69, 1000000):
        if is_property(num):
            count += 1
    return count


if __name__ == "__main__":
    print(answer())
