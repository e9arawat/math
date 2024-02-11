"""Problem 48"""


def solver():
    """Self Powers"""
    digits = 10**10
    numbers = (pow(i, i, digits) for i in range(1, 1000 + 1))
    ans = sum(numbers) % digits
    return ans


if __name__ == "__main__":
    print(solver())
