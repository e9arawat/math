"""Problem 40"""


def solver():
    """return Champernowne's Constant"""
    temp = "0"
    num = 1
    while len(temp) < 1000001:
        temp += str(num)
        num += 1
    return (
        int(temp[1])
        * int(temp[10])
        * int(temp[100])
        * int(temp[1000])
        * int(temp[10000])
        * int(temp[100000])
        * int(temp[1000000])
    )


if __name__ == "__main__":
    print(solver())
