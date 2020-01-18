import numpy as np
grid = np.array([[0, 0, 0], [1, 0, 0], [2, 0, 0]])

new = grid.tolist()
for i in range(3):
    for j in range(3):
        if grid[i][j] == 1:
            new[i][j] = "X"
        if grid[i][j] == 2:
            new[i][j] = "O"
print()
