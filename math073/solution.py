""" 
Counting Fractions in a Range
"""


def answer():
    """
    Counting Fractions in a Range
    """
    ans = 0
    stack = [(1, 3, 1, 2)]
    while len(stack) > 0:
        left_num, left_den, right_num, right_den = stack.pop()
        den = left_den + right_den
        if den <= 12000:
            num = left_num + right_num
            ans += 1
            stack.append((num, den, right_num, right_den))
            stack.append((left_num, left_den, num, den))
    return str(ans)


if __name__ == "__main__":
    print(answer())
