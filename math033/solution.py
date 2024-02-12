"""Day-33"""


def find_denominator(i, j):
    """function to find smallest denominator"""
    temp = i
    while temp:
        if i % temp == 0 and j % temp == 0:
            return j // temp
        temp -= 1
    return j


def check_trival(i, j):
    """function to find trival number"""
    temp1 = i / j
    list1 = [*str(i)]
    list2 = [*str(j)]

    dict1 = {x: list1.count(x) for x in set(list1)}
    dict2 = {x: list2.count(x) for x in set(list2)}

    num1, num2 = [], []
    for x in list1:
        if x not in list2:
            num1.append(x)
        elif dict1[x] > dict2[x]:
            num1.append(x)
            dict1[x] -= 1

    dict1 = {x: list1.count(x) for x in set(list1)}
    dict2 = {x: list2.count(x) for x in set(list2)}

    for x in list2:
        if x not in list1:
            num2.append(x)
        elif dict2[x] > dict1[x]:
            num2.append(x)
            dict2[x] -= 1

    num1 = "".join(num1) or 1
    num2 = "".join(num2) or 1

    if num1 == 1 or num1 == str(i):
        return 1

    temp2 = int(num1) / int(num2)
    if temp1 == temp2:
        return find_denominator(i, j)

    return 1


def answer():
    """function to find product of all trival"""
    ans = 1
    for i in range(11, 100):
        for j in range(i + 1, 100):
            if i % 10 == 0 or j % 10 == 0 or i / j >= 1:
                continue
            ans *= check_trival(i, j)

    return ans


if __name__ == "__main__":
    print(answer())
