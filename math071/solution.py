""" 
Ordered Fractions
"""


def answer():
    """
    Ordered Fractions

    0/1, 1/1 -> 0+1/1+1 -> 1/2 (larger than 3/7)
    0/1, 1/2 -> 0+1/1+2 -> 1/3 (smaller that 3/7)
    1/3, 1/2 -> 1+1/3+2 -> 2/5 (smaller that 3/7)
    .
    .
    .
    2/5, 3/7 -> 2+3/5+7 -> 5/12 (larger that 3/7)
    ....
    after this there is a pattern in all the other fraction.
    Every fraction is the addition of (2/5, 3*x/7*x) -> (2+3*x)/ (5+7*x)

    Also we know that the max denominator is 1000000

    So 5+7*x = 1000000 -> x = 142856

    therefore, putting value of x in numerator
    2+3*x -> 2+3*142857 -> 428570

    """

    denominator = 1000000
    x = (denominator - 5) // 7
    return 2 + 3 * x


if __name__ == "__main__":
    print(answer())
