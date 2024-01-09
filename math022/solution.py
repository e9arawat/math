"""Day-22 Name Scores"""
import string


def solver(filename):
    """function to find name score"""
    alphabets = list(string.ascii_lowercase)
    alphabets_place = {x: i for i, x in enumerate(alphabets, start=1)}
    with open(filename, "r", encoding="utf8") as f:
        data = f.read()

    data = data.replace(",", " ").replace('"', " ").split()
    data = sorted(data)
    ans = 0
    for index, val in enumerate(data, start=1):
        sum_of_chars = 0
        for x in val:
            sum_of_chars += alphabets_place[x.lower()]
        ans = ans + (sum_of_chars * index)

    return ans


def answer():
    """calling solver function"""
    return solver("names.txt")


if __name__ == "__main__":
    print(answer())
    print(solver("names.txt"))
