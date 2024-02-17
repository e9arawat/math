""" 
Square Root Convergents
"""


def answer():
    """
    Square Root Convergents
    """

    prev_den = 1
    prev_num = 1
    count = 0
    for _ in range(1000):
        current_den = 1 * prev_den + prev_num
        current_num = 1 * current_den + prev_den

        if len(str(current_num)) > len(str(current_den)):
            count += 1
        prev_den = current_den
        prev_num = current_num

    return count


if __name__ == "__main__":
    print(answer())
