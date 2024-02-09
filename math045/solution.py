"""Problem 45"""

def solver():
    """return Triangular, Pentagonal, and Hexagonal"""
    hexagonal = [(n*(2*n-1)) for n in range(285, 100000)]
    for n in range(165, 32001):
        temp = (n*(3*n-1))//2
        if temp in hexagonal:
            return temp
    


if __name__ == "__main__":
    print(solver())