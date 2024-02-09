"""Problem 36"""


def find_binary(num):
    """return binary form of a number"""
    ans = ""
    while num > 1:
        ans = str(num % 2) + ans
        num = num // 2
    return "1" + ans


def is_palindrome(num):
    """return if the number is palindrome or not"""
    return num == num[::-1]


def solver(n):
    """return the sum of Double-base Palindromes"""
    ans = 0
    for i in range(1, n):
        if is_palindrome(str(i)) and is_palindrome(find_binary(i)):
            ans += i

    return ans


if __name__ == "__main__":
    print(solver(1000000))
