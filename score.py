import os
import subprocess
def score():
    current_dir = os.getcwd()
    dir_list = os.listdir(current_dir)
    dir_list = sorted(dir_list)
    for dir in dir_list:  
        if 'math' not in dir:
            continue
        print(dir)
        next_dir = dir + "/solution.py"
        os.system('python3 '+next_dir)
        
    
if __name__ == "__main__":
    score() 
