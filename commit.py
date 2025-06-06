import subprocess
import os
import random
import numpy as np
import datetime
import time
import random

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
        delay = int(random.random()*20)
        print(f"Commit {i}, sleep for {delay}s")
        time.sleep(delay)


def main():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    grid = np.loadtxt(f"{script_dir}/pattern.csv", delimiter=",")
    githubdays = [
        1, 2, 3, 4, 5, 6, 0
    ]
    week_number = datetime.date.today().isocalendar().week
    weekday = datetime.date.today().weekday() # starts at 0

    githubday = githubdays[weekday]
    ncommits = int(grid[githubday][week_number])
    print(f"\nWeek: {week_number}, Day: {weekday}, GithubDay: {githubday}, Commits: {ncommits}\n")
    commit(ncommits, script_dir)
        
    
if __name__ == "__main__":
    main()
