"""function to find sum of all prime numbers"""


def solver(p: int, q: int = None):
    """function"""
    start, end = 2, p
    if q:
        start, end = p, q
    if start > end or end < 2:
        return None
    start_sum, end_sum = 0, 0
    # finding for start
    prime_list_start = start * [1]
    for i in range(2, int(start**0.5) + 1):
        if prime_list_start[i] == 1:
            for j in range(i, start):
                if i * j < start:
                    prime_list_start[i * j] = 0
                else:
                    break
    # finding for end
    prime_list_end = end * [1]
    for i in range(2, int(end**0.5) + 1):
        if prime_list_end[i] == 1:
            for j in range(i, end):
                if i * j < end:
                    prime_list_end[i * j] = 0
                else:
                    break

    for i, val in enumerate(prime_list_start):
        if val == 1:
            start_sum += i

    for i, val in enumerate(prime_list_end):
        if val == 1:
            end_sum += i

    ans = end_sum - start_sum
    return ans


def answer():
    """calling solver function"""
    return solver(2000000)


if __name__ == "__main__":
    print(answer())
    print(solver(3, 10000))
