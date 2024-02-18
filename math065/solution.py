""" 
Convergent of e
"""


def e_convergent(i):
    """
    return the continuous fraction
    """
    if i == 0:
        return 2
    if i % 3 == 2:
        return i // 3 * 2 + 2
    return 1


def answer():
    """
    Convergent of e
    """
    num = 1
    den = 0
    for i in reversed(range(100)):
        num, den = e_convergent(i) * num + den, num
    ans = sum(int(c) for c in str(num))
    return str(ans)


if __name__ == "__main__":
    print(answer())
