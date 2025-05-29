import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import os
import argparse

characters5 = {
    "A": [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
    ],
    "B": [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ],
    "C": [
        [0,1,1,1],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,1,1,1],
    ],
    "D": [
        [1,1,1,0],
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,0],
    ],
    "E": [
        [1,1,1],
        [1,0,0],
        [1,1,1],
        [1,0,0],
        [1,1,1],
    ],
    "F": [
        [1,1,1],
        [1,0,0],
        [1,1,1],
        [1,0,0],
        [1,0,0],
    ],
    "G": [
        [1,1,1,0],
        [1,0,0,0],
        [1,0,1,1],
        [1,0,0,1],
        [1,1,1,1],
    ],
    "H": [
        [1,0,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
    ],
    "I": [
        [1,],
        [1,],
        [1,],
        [1,],
        [1,],
    ],
    "J": [
        [0,0,1,],
        [0,0,1,],
        [0,0,1,],
        [1,0,1,],
        [0,1,1,]
    ],
    "K": [
        [1,0,0,1],
        [1,0,1,0],
        [1,1,1,0],
        [1,0,1,0],
        [1,0,0,1],
    ],
    "L": [
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,1,1],
    ],
    "M": [
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    "N": [
        [1,0,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,1],
    ],
    "O": [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
    ],
    "P": [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ],
    "Q": [
        [1, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1]
    ],
    "R": [
        [1,1,1],
        [1,0,1],
        [1,1,0],
        [1,0,1],
        [1,0,1],
    ],
    "S": [
        [1,1,1,],
        [1,0,0,],
        [1,1,1,],
        [0,0,1,],
        [1,1,1,],
    ],
    "T": [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    "U": [
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,1,1],
    ],
    "V": [
        [1,0,0,1],
        [1,0,0,1],
        [1,0,0,1],
        [0,1,1,0],
        [0,0,1,0]
    ],
    "W": [
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,1,0,1,1],
    ],
    "X": [
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1]
    ],
    "Y": [
        [1, 0, 0, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ],
    "Z": [
        [1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0],
        [1, 1, 1, 1, 1]
    ],
    "!": [
        [1],
        [1],
        [1],
        [0],
        [1],
    ],    
}

def write(text, script_dir):
    grid = np.random.randint(8, 15, (7,52))
    figure(figsize=(15, 4), dpi=80)
    idx = 1
    for i in range(len(text)):
        crr = text[i]
        if crr== " ":
            idx += 1
        else:
            arr = np.array(characters5[crr])
            x = arr.shape[1]
            grid[1:6, idx:idx+x] = (np.array(characters5[crr])*40+ np.random.randint(8, 15, (5,x)))
            idx += x
            if i<len(text) -1:
                if text[i+1] != "T":
                    idx += 1
                else:
                    if text[i] == "I":
                        idx += 1                        
        if idx>52-5:
            idx = 0
            
    np.savetxt(f"{script_dir}/pattern.csv", grid, delimiter=",")
    plt.imshow(grid, cmap='gray', vmin=0, vmax=40)
    plt.savefig(f"{script_dir}/pattern.jpg")
    print(f"Saved {script_dir}/pattern.csv")
    plt.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=""
    )
    parser.add_argument("message", type=str, help="The text you want to generate/display")
    args = parser.parse_args()
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    write(args.message, script_dir)
    