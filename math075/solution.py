""" 
Singular Integer Right Triangles
"""
import math


def gcd(m, n):
    """
    return the gcd of the numbers
    """
    if n == 0:
        return m
    return gcd(n, m % n)


def answer():
    """
    Singular Integer Right Triangles
    """

    triangles = [0] * (1500001)

    for m in range(2, int(math.sqrt(1500000))):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a = m**2 - n**2
                b = 2 * m * n
                c = m**2 + n**2
                length = a + b + c

                k_length = length
                while k_length <= 1500000:
                    triangles[k_length] += 1
                    k_length += length

    return triangles.count(1)


if __name__ == "__main__":
    print(answer())
