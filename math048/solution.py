"""Problem 48"""


def find_power(num):
    """return num to the power num"""
    ans = str(num)
    for i in range(1, num):
        temp_ans = ""
        remainder = 0
        for i in ans[::-1]:
            total = remainder + num * int(i)
            temp_ans = str(total % 10) + temp_ans
            remainder = total // 10
        if remainder:
            temp_ans = str(remainder) + temp_ans
        ans = temp_ans
        if len(ans) > 10:
            ans = ans[-10:]
    return int(ans)


def answer():
    """Self Powers"""
    mod = 10**10
    all_nums = [find_power(i) for i in range(1, 1001)]
    return sum(all_nums) % mod


# def solver():
#     """Self Powers"""
#     digits = 10**10
#     numbers = (pow(i, i, digits) for i in range(1, 1000 + 1))
#     ans = sum(numbers) % digits
#     return ans


if __name__ == "__main__":
    print(answer())
