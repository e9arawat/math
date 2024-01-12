"""Day-25"""
def add_terms(num1: str, num2: str):
    """function to add two numbers"""
    index, result, remainder = 1, "", 0
    while index <= len(num2):
        d1, d2 = 0, int(num2[-index])
        if index <= len(num1):
            d1 = int(num1[-index])
        digits_sum = d1 + d2 + remainder
        result = str(digits_sum % 10) + result
        remainder = digits_sum // 10
        index += 1
    if remainder:
        result = str(remainder) + result
    return result


def solver(term):
    """function to find index of first fibonacii number having term digits"""
    fibonacii_list = ["0", "1"]
    while len(fibonacii_list[-1]) < term:
        fibonacii_list.append(add_terms(fibonacii_list[-2], fibonacii_list[-1]))

    return len(fibonacii_list) - 1


def answer():
    """calling solver function"""
    return solver(1000)


if __name__ == "__main__":
    print(answer())
    print(solver(3))
