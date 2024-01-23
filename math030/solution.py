"""Day-30"""


def solver(n):
    """function to find sum of all the numbers"""
    ans = 0
    for i in range(2, 10000000):
        temp, index = i, 0
        current_sum = 0
        while temp:
            current_num = temp % 10
            current_num = current_num**n
            current_sum += current_num
            if current_sum > i:
                break
            index += 1
            temp = temp // 10
        if current_sum == i:
            ans += current_sum
    return ans


def answer():
    """calling solver function"""
    return solver(5)


if __name__ == "__main__":
    print(answer())
    print(solver(3))
