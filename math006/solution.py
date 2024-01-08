"""function to find difference"""


def solver(start, end):
    """function to find sum of n natural numbers"""
    sum_start, sum_end = (start * (start - 1)) // 2, (end * (end + 1)) // 2
    sum_square_start, sum_square_end = (
        start * (start - 1) * (2 * (start - 1) + 1)
    ) // 6, (end * (end + 1) * (2 * end + 1)) // 6
    sum_square = sum_square_end - sum_square_start
    square_sum = (sum_end - sum_start) ** 2
    return square_sum - sum_square


def answer():
    """calling solver function"""
    return solver(1, 10)


if __name__ == "__main__":
    print(answer())
    print(solver(1, 100))
