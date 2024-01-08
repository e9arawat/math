"""script to runn all math problems"""
import os


def score():
    """function"""
    dir_list = sorted(os.listdir(os.getcwd()))
    for x in dir_list:
        if "math" not in x:
            continue
        print(dir)
        next_dir = x + "/solution.py"
        os.system("python3 " + next_dir)


if __name__ == "__main__":
    score()
