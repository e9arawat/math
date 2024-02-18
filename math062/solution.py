""" 
Cubic Permutations
"""


def answer():
    """
    Cubic Permutations
    """
    primes = {}
    n = 1
    while True:
        k = n**3
        key = "".join(sorted(str(k)))
        primes[key] = primes.get(key, []) + [k]
        if len(primes[key]) == 5:
            return min(primes[key])
        n += 1


if __name__ == "__main__":
    print(answer())
