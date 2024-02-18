""" 
Powerful Digit Counts
"""


def answer():
    """
    Powerful Digit Counts
    """
    count = 0
    for a in range(1000):
        num = 1
        while True:
            temp = num**a
            if len(str(temp)) > a:
                break
            if len(str(temp)) == a:
                count += 1
            num += 1
    return count


if __name__ == "__main__":
    print(answer())
