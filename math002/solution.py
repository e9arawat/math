"""Day-2"""


def solver(start, end, even=False, odd=False):
    """Base condition"""
    if start > end:
        return None
    if even is False and odd is False:
        return 0
    # Initializing variables
    a = 0
    b = 1
    c = a + b
    ans = 0
    odd_sum = 0
    even_sum = 0
    # Iterating to the start point
    while c < start:
        a = c
        c += b
        b = a
    # Checking for the start and end point
    while start <= c <= end:
        if c % 2 == 0:
            even_sum += c
        else:
            odd_sum += c
        a = c
        c += b
        b = a
    # Checking if even/odd term should be included to not
    if even is True:
        ans += even_sum
    if odd is True:
        ans += odd_sum

    return ans


def answer():
    """answer"""
    a = 0
    b = 1
    c = a + b
    ans = 0
    while c < 4000000:
        if c % 2 == 0:
            ans += c
        a = c
        c += b
        b = a
    return ans


if __name__ == "__main__":
    print(answer())
    print(solver(15812, 91581312, True, False))
