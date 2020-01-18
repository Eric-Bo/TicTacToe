from Player import Player
import numpy as np


class Board:

    """the board class that keeps track of the symbols on the board
    0=leer
    1=X
    2=O    
    """
    def __init__(self):
        self.grid = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    def insert(self,  row, col, arg):
        if self.grid[row][col] == 0:
            self.grid[row][col] = arg
            return True
        else:
            return False

    def winner(self):
        winner = None
        # check for horizontal and vertical win
        for i in range(3):
            if self.grid[i].tolist().count(1) == 3 or self.grid[:, i].tolist().count(1) == 3:
                winner = Player("X")
                break
            if self.grid[i].tolist().count(2) == 3 or self.grid[:, i].tolist().count(2) == 3:
                winner = Player("O")
                break

        # check for vertical win
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == 1 or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == 1:
            winner = Player("X")
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] == 2 or self.grid[0][2] == self.grid[1][1] == self.grid[2][0] == 2:
            winner = Player("X")
        return winner

    def pretty_print(self):
        """makes the grid more readable for the user"""
        new = self.grid.tolist()
        final_string = ""
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == 1:
                    new[i][j] = "X"
                if self.grid[i][j] == 2:
                    new[i][j] = "O"
                final_string = final_string + str(new[i][j])
            final_string = final_string + "\n"
        return final_string
