"""Day-26"""


def find_reciprocal(num, reciprocal_list):
    """function to find longest length of decimal part"""
    remainder, quotient, temp = [], "0.", 10
    while temp not in remainder and temp != 0:
        remainder.append(temp)
        while temp < num:
            quotient += "0"
            temp *= 10
        quotient += str(temp // num)
        temp = temp % num
        temp *= 10

    reciprocal_list.append(quotient[2:])
    return len(quotient) - 2


def solver(n, input_list: list = None):
    """function to find reciprocal"""
    max_length, reciprocal_list = 0, []
    for i in range(2, n + 1):
        max_length = max(max_length, find_reciprocal(i, reciprocal_list))

    if not input_list:
        return max_length
    count = 0
    for x in reciprocal_list:
        if input_list[0] in x:
            count += 1
    return count


def answer():
    """calling solver function"""
    return solver(1000)


if __name__ == "__main__":
    print(answer())
    print(solver(1000, ["142857"]))
