import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib as mpl
import os

characters5 = {
    "I": [
        [1,],
        [1,],
        [1,],
        [1,],
        [1,],
    ],
    "C": [
        [0,1,1,1],
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0],
        [0,1,1,1],
    ],
    "O": [
        [0,1,1,1,0],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [0,1,1,1,0],
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
    "M": [
        [1,1,0,1,1],
        [1,0,1,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
    ],
    "T": [
        [1,1,1,1,1],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
        [0,0,1,0,0],
    ],
    "!": [
        [1],
        [1],
        [1],
        [0],
        [1],
    ],
    "S": [
        [1,1,1,],
        [1,0,0,],
        [1,1,1,],
        [0,0,1,],
        [1,1,1,],
    ],
    "G": [
        [1,1,1,0],
        [1,0,0,0],
        [1,0,1,1],
        [1,0,0,1],
        [1,1,1,1],
    ],
    "F": [
        [1,1,1],
        [1,0,0],
        [1,1,1],
        [1,0,0],
        [1,0,0],
    ],
    "A": [
        [1,1,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
    ],
    "U": [
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,0,1],
        [1,1,1],
    ],
    "L": [
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,1,1],
    ],
    "H": [
        [1,0,1],
        [1,0,1],
        [1,1,1],
        [1,0,1],
        [1,0,1],
    ],
    "K": [
        [1,0,0,1],
        [1,0,1,0],
        [1,1,1,0],
        [1,0,1,0],
        [1,0,0,1],
    ],
    "R": [
        [1,1,1],
        [1,0,1],
        [1,1,0],
        [1,0,1],
        [1,0,1],
    ],
    "N": [
        [1,0,0,0,1],
        [1,1,0,0,1],
        [1,0,1,0,1],
        [1,0,0,1,1],
        [1,0,0,0,1],
    ],
}

def write(text):
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

    plt.imshow(grid, cmap='gray', vmin=0, vmax=40)
    plt.show()
    return grid

# write("I CODE")
# write("SEGFAULT")
# write("COMMIT!")
text="HACKERMAN"
grid = write(text)
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
np.savetxt(f"{script_dir}/{text}.csv", grid, delimiter=",")
print(f"Saved {script_dir}/{text}.csv")