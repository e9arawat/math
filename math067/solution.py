""" 
Maximum Path Sum II
"""


def answer():
    """
    Maximum Path Sum II
    """

    with open("0067_triangle.txt", "r", encoding="UTF-8") as file:
        triangle = []
        for line in file:
            triangle.append([int(num) for num in line.split()])

    sums = [0]

    for row in triangle:
        new_sums = [
            row[0] + sums[0],
            *[row[i] + max(sums[i - 1], sums[i]) for i in range(1, len(row) - 1)],
            row[-1] + sums[-1],
        ]
        sums = new_sums

    max_sum = max(sums)
    return max_sum


if __name__ == "__main__":
    print(answer())
