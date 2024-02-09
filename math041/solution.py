"""Problem 41"""
#7652413

def is_prime(num):
    """return if the number is prime or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_pandigital(num):
    """return if numbers is pan digital or not"""
    num = sorted(str(num))
    for index, x in enumerate(num):
        if x in num[index+1:] or int(x) > len(num):
            return False
    return True

def solver():
    """return the largest pandigital prime"""
    for i in reversed(range(2, 10000000)):
        if '0' not in str(i) and is_pandigital(i) and is_prime(i):
            return i
        

if __name__ == "__main__":
    print(solver())