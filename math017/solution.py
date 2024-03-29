"""python program to find number of letters that would be used to write """

words_dict = {
    100000000: "billion",
    1000000: "million",
    1000: "thousand",
    100: "hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "forty",
    30: "thirty",
    20: "twenty",
    19: "nineteen",
    18: "eighteen",
    17: "seventeen",
    16: "sixteen",
    15: "fifteen",
    14: "fourteen",
    13: "thirteen",
    12: "twelve",
    11: "eleven",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
}


def find_length(num):
    """function to find lenght of each number in words"""
    if num == 0:
        return 0
    if num in words_dict:
        if num % 100 == 0:
            return len(words_dict[num]) + 3
        return len(words_dict[num])
    ans = 0
    for key, value in words_dict.items():
        if num >= key:
            if num >= 100:
                ans += find_length(num // key)
            ans += len(value) + find_length(num % key)
            return ans
    return 0


def solver(n: int = 1, m: int = 1000):
    """function to find length of all number in words"""
    start, end = 1, n
    if m:
        start, end = n, m
    ans = 0
    for i in range(start, end + 1):
        if i > 100 and i % 100 != 0:
            ans += 3
        ans += find_length(i)
    return ans


def answer():
    """calling solver function"""
    return solver(1, 1000)


if __name__ == "__main__":
    print(answer())
    print(solver(1, 10000))
