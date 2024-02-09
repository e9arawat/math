"""Problem 48"""

def find_sum(ans, square):
    result = ""
    index = 1
    remainder = 0
    while index <= len(square):
        total = remainder + int(ans[-index]) + int(square[-1])
        result = total % 10
        remainder = total // 10
        index += 1
    while(remainder):
        total = remainder + 


def find_square(num):
    ans = ""
    temp = num
    remainder = 0
    while temp:
        product = remainder + (temp % 10) * num
        ans = str((product%10)) + ans
        remainder = product // 10
        temp = temp // 10
    if remainder:
        ans = str(remainder) + ans
    return ans

def solver():
    """Self Powers"""
    number = ""
    for i in range(1, 1001):
        square = find_square(i)
        ans = find_sum(ans, square)