"""function to find number between p and q having longest Collatz Sequence"""


def solver(p: int = None, q: int = None):
    """we are creating a dictionary where we are storing
    the length of the sequence of each number that we are checking at the moment
    so next time when we get the same number in the middle of another sequence we
    can directly take the rest of the length
    """
    if not p and not q:
        return None
    if p and not q:
        start, end = 2, p
    else:
        start, end = min(p, q), max(p, q)

    sequence_dict = {}
    max_lenght, ans = 0, 0
    for i in range(start, end + 1):
        temp_num, temp_length = i, 0
        while temp_num > 1:
            temp_length += 1
            if temp_num % 2 == 0:
                temp_num = temp_num // 2
            else:
                temp_num = temp_num * 3 + 1
            if temp_num in sequence_dict:
                temp_length += sequence_dict[temp_num]
                break

        if max_lenght < temp_length:
            max_lenght = temp_length
            ans = i
        sequence_dict[i] = temp_length

    return ans


def answer():
    """calling solver function"""
    return solver(1000000)


if __name__ == "__main__":
    print(answer())
    print(solver(1, 10000))
