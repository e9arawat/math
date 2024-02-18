""" 
Diophantine Equation
"""
import math

def find_x(D, y):
    return math.sqrt(1 + (D * (y**y)))

def is_square(D):
    return D**0.5 == int(D**0.5)

def answer():
    """ 
    Diophantine Equation
    """
    max_x = max_x_d = 0
    for D in range(8):
        if is_square(D):
            continue
        y = 1
        while True:
            x = find_x(D, y)
            if x != int(x):
                continue
            print(x, y)
            if x**2 - (D * (y**y)) == 1 and max_x < x:
                max_x = x
                max_x_d = D
                break
            y += 1
    return max_x_d

if __name__ == "__main__":
    print(answer())