"""Problem 43"""


def is_property(num):
    """return if number satisfy the property"""
    divisors = [2, 3, 5, 7, 11, 13, 17]
    index = 0
    while index < 7:
        if int(num[index : index + 3]) % divisors[index] != 0:
            return False
        index += 1
    return True


def all_combinations(combinations, digits, remaining_digits):
    """function to find all the combinations of a given number"""
    if len(remaining_digits) == 0:
        combinations.append(int(digits))
        return
    for index, x in enumerate(remaining_digits):
        if digits == "" and x == "0":
            continue
        all_combinations(
            combinations,
            digits + remaining_digits[index],
            remaining_digits[:index] + remaining_digits[index + 1 :],
        )


def answer():
    """return sum of all Sub-string Divisibility numbers"""
    ans = 0
    combinations = []
    number = "0123456789"
    all_combinations(combinations, "", number)
    for i in combinations:
        if is_property(str(i)[1:]):
            ans += i

    return ans


if __name__ == "__main__":
    print(answer())
