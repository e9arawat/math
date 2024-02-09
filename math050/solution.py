"""Problem 50"""

def solver():
    """return the Consecutive Prime Sum"""
    all_primes = [x for x in range(2,1000) if all(x%i!=0 for i in range(2,int(x**0.5)+1))]

    max_sum = 0
    temp = 0
    for i in range(len(all_primes)):
        temp = 0
        for x in all_primes[i+1:]:
            temp += x
            if temp in all_primes:
                max_sum = max(max_sum, temp)
    return max_sum

if __name__ == "__main__":
    print(solver())