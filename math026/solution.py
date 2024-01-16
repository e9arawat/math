"""Day-26"""


def find_reciprocal(num, reciprocal_dict):
    """function to find longest length of decimal part"""
    remainder, quotient, temp = [], "", 10
    while temp not in remainder and temp != 0:
        remainder.append(temp)
        while temp < num:
            quotient += "0"
            temp *= 10
        quotient += str(temp // num)
        temp = temp % num
        temp *= 10
    if temp == 0:
        reciprocal_dict[num] = quotient
    else:
        for index, n in enumerate(remainder):
            if n == temp:
                reciprocal_dict[num] = quotient[index:]
    return len(quotient) - 2


def solver(n, input_list: list = None):
    """function to find reciprocal"""
    max_length, reciprocal_dict = 0, {}
    ans = 2
    for i in range(2, n + 1):
        decimal_length = find_reciprocal(i, reciprocal_dict)
        if max_length < decimal_length:
            max_length = decimal_length
            ans = i

    if not input_list:
        return ans
    for key, value in reciprocal_dict.items():
        if value == str(input_list[0]):
            return key
    return 0


def answer():
    """calling solver function"""
    return solver(1000)


if __name__ == "__main__":
    print(answer())
    print(solver(1000, [142857]))
