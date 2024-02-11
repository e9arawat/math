"""Problem 41"""


def is_prime(num):
    """return if the number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def all_combinations(combinations, digits, remaining_digits):
    """function to find all the combinations of a given number"""
    if len(remaining_digits) == 0:
        if is_prime(int(digits)):
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


def solver():
    """return the largest pandigital prime"""
    number = "123456789"
    for _ in range(8):
        combinations = []
        all_combinations(combinations, "", number)
        if combinations:
            return max(combinations)
        number = number[:-1]
    return 0


if __name__ == "__main__":
    print(solver())
