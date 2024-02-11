"""Problem 40"""


def solver():
    """return Champernowne's Constant"""
    temp = "0"
    for num in range(1, 185186):
        temp += str(num)
    index = "1"
    ans = 1
    for _ in range(7):
        ans *= int(temp[int(index)])
        index += "0"
    return ans


if __name__ == "__main__":
    print(solver())
