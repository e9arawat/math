"""Day-29"""


def solver(n):
    """function to find distinct elements"""
    result = set()
    for i in range(2, n + 1):
        temp = str(i)
        for _ in range(2, n + 1):
            remainder, index, num = 0, 1, ""
            while index <= len(temp):
                mul = int(temp[-index]) * i
                mul += remainder
                num = str(mul % 10) + num
                remainder = mul // 10
                index += 1
            if remainder:
                num = str(remainder) + num
            result.add(num)
            temp = num

    return len(result)


def answer():
    """calling solver function"""
    return solver(100)


if __name__ == "__main__":
    print(answer())
    print(solver(5))
