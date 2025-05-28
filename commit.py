import subprocess
import os
import random
import numpy as np
import datetime
import time

def commit(ncommits, script_dir):
    words = [
        "Banana!", "Hello World!", "Creeper!", "Code like a boss!",
        "Duck!", "42 is the answer!", "Eat more RAM!", "Now in HD!",
        "Infinite bugs!", "To the moon!", "Bug-free!"
    ]
    commit_message = random.choice(words)
    for i in range(ncommits):
        data = np.random.randint(0, 64, (2, 2))
        np.save(f"{script_dir}/encrypted.npy", data)
        subprocess.run(["git", "add", "."], cwd=script_dir)
        subprocess.run(["git", "commit", "-am", commit_message], cwd=script_dir)
        subprocess.run(["git", "push"], cwd=script_dir)


def main():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    text="HACKERMAN"
    grid = np.loadtxt(f"{script_dir}/{text}.csv", delimiter=",")
    githubdays = [
        1, 2, 3, 4, 5, 6, 0
    ]
    week_number = datetime.date.today().isocalendar().week
    weekday = datetime.date.today().weekday()

    weekday = githubdays[weekday]
    ncommits = int(grid[weekday][week_number])
    commit(1, script_dir)
        
    
if __name__ == "__main__":
    main()
