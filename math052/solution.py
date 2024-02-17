"""
Permuted Multiples
"""


def answer():
    """
    Permuted Multiples
    """
    num = 1
    while True:
        test = sorted(str(num))
        for i in range(2, 7):
            temp = num * i
            flag = True
            if sorted(str(temp)) != test:
                flag = False
                break
        if flag:
            return num
        num += 1


if __name__ == "__main__":
    print(answer())
