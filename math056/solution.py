""" 
Powerful Digit Sum
"""


def answer():
    """
    Powerful Digit Sum
    """
    max_sum = 0
    for a in range(100):
        for b in range(100):
            num = a**b
            temp = sum(int(x) for x in str(num))
            max_sum = max(max_sum, temp)
    return max_sum


if __name__ == "__main__":
    print(answer())
