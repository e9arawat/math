"""function to find all Pythagorean triplet"""


def solver(p: int, q: int = None):
    """return dictionary of list of tuples"""
    ans, c, i, start, end = {}, 0, 2, 1, p
    if q:
        start, end = p, q
    while c < end:
        for j in range(1, i + 1):
            a = i * i - j * j
            b = 2 * i * j
            c = i * i + j * j
            if c > end:
                break
            if a == 0 or b == 0 or c == 0 or a + b + c < start or a + b + c > end:
                break
            temp = (a, b, c)
            temp = sorted(temp)
            temp = tuple(temp)
            ans[a + b + c] = [temp]
        i += 1
    ans = dict(sorted(ans.items()))
    return ans


def answer():
    """function to find product"""
    ans = 0
    flag = 0
    num_list = list(range(1, 1001))
    for i in range(0, len(num_list) - 2):
        if flag:
            break
        j, k = i + 1, len(num_list) - 1

        while j < k:
            if (num_list[i] + num_list[j] + num_list[k] == 1000) and (
                (num_list[i] < num_list[j] < num_list[k])
                and (num_list[i] ** 2 + num_list[j] ** 2 == num_list[k] ** 2)
            ):
                ans = num_list[i] * num_list[j] * num_list[k]
                flag = 1
                break
            if num_list[i] + num_list[j] + num_list[k] > 1000:
                k -= 1
            else:
                j += 1
    return ans


if __name__ == "__main__":
    print(answer())
    print(solver(2, 78))
