"""
Lychrel Numbers
"""


def is_palindrome(num):
    """
    return if the number is palindrome or not
    """
    return str(num) == str(num)[::-1]


def answer():
    """
    Lychrel Numbers
    """
    count = 0
    for num in range(10001):
        flag = True
        for _ in range(50):
            num += int(str(num)[::-1])
            if is_palindrome(num):
                flag = False
                break
        if flag:
            count += 1
    return count


if __name__ == "__main__":
    print(answer())
