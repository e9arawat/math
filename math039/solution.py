"""Problem 39"""

def solver():
    """return the maximum number for which the number of solutions maximised"""
    ans =  max_solution = 0

    pythagorean_triplets = []
    a = 1
    while a < 333:
        b = a+1
        