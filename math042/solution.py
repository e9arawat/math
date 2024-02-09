"""Problem 42"""
import string


def solver(filename):
    """return the total triangular words"""
    with open(filename, "r", encoding="UTF-8") as f:
        data = f.read()
    ans = 0
    data = data.replace('"', " ").replace(",", " ").split()
    all_letters = string.ascii_lowercase.replace("", " ").split()
    letters_dict = {x: index + 1 for index, x in enumerate(all_letters)}
    trialgle_numbers = [(n * (n + 1)) // 2 for n in range(1, 1000000)]
    for word in data:
        current_number = sum(letters_dict[x.lower()] for x in word)
        if current_number in trialgle_numbers:
            ans += 1
    return ans


if __name__ == "__main__":
    print(solver("words.txt"))
