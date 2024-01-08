"""function to find the first triangle number which has 500 or more factors"""


def find_factors(current_number, limit):
    """function to check for factors"""
    count = 0
    temp_range = int(current_number**0.5) + 1
    for i in range(1, temp_range):
        if current_number % i == 0:
            count += 1
    if int(current_number**0.5) == current_number**0.5:
        count = ((count - 1) * 2) + 1
    else:
        count *= 2
    return bool(count > limit)


def solver(n):
    """functionj to find the triangle number"""
    current_number, iterator = 0, 1
    while True:
        current_number += iterator
        if find_factors(current_number, n):
            return current_number
        iterator += 1


def answer():
    """calling solver sunction"""
    return solver(500)


if __name__ == "__main__":
    print(answer())
    print(solver(4))
