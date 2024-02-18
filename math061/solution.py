"""
Cyclical Figurate Numbers
"""


def answer():
    """
    Cyclical Figurate Numbers
    """
    triangles = [(n * (n + 1)) // 2 for n in range(45, 141)]
    squares = [n**n for n in range(32, 100)]
    pentagonal = [(n * (3 * n - 1)) // 2 for n in range(26, 82)]
    hexagonal = [(n * (2 * n - 1)) // 2 for n in range(23, 70)]
    heptagonal = [(n * (5 * n - 3)) // 2 for n in range(21, 64)]
    octagonal = [(n * (3 * n - 2)) // 2 for n in range(19, 59)]
