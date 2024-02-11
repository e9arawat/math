"""Problem 42"""

import string
import math


def is_triangle(num):
    """return if the number is triangle or not"""
    n = (math.sqrt(1 + 8 * num) - 1) / 2
    if n == int(n):
        return True
    return False


def solver(filename):
    """return the total triangular words"""
    with open(filename, "r", encoding="UTF-8") as f:
        data = f.read()
    ans = 0
    data = data.replace('"', " ").replace(",", " ").split()
    all_letters = string.ascii_lowercase.replace("", " ").split()
    letters_dict = {x: index + 1 for index, x in enumerate(all_letters)}
    for word in data:
        current_number = sum(letters_dict[x.lower()] for x in word)
        if is_triangle(current_number):
            ans += 1
    return ans


if __name__ == "__main__":
    print(solver("words.txt"))
