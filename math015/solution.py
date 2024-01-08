"""function to find total unique paths"""


from collections import deque


def solver(n, m):
    """by taking the approach that every index can be reached by 2 ways
    n, m = n + 1, m + 1
    matrix = [[0 for _ in range(m)] for j in range(n)]
    for i in range(n):
        matrix[i][0] = 1
    for i in range(m):
        matrix[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[n - 1][m - 1]"""

    n, m = n + 1, m + 1
    arr = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    matrix = [[-1 for _ in range(m)] for j in range(n)]
    queue_list = deque([[0, 0]])
    matrix[0][0] = 1
    while queue_list:
        a, b = queue_list[0][0], queue_list[0][1]
        queue_list.popleft()
        for i in range(0, 2):
            x, y = a + arr[i][0], b + arr[i][1]
            if x >= 0 and y >= 0:
                matrix[a][b] += matrix[x][y]
        for i in range(2, 4):
            x, y = a + arr[i][0], b + arr[i][1]
            if x < n and y < m and matrix[x][y] == -1:
                matrix[x][y] = 0
                queue_list.append([x, y])
    return matrix[n - 1][m - 1]


def answer():
    """calling solver function"""
    return solver(20, 20)


if __name__ == "__main__":
    print(answer())
    print(solver(4, 4))
