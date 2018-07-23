"""
Depth-first Search on a 2D grid

Note: 'steps' indicates order of expansion, not distance from the source cell.

Jessica Yung
Jan 2018
"""
import numpy as np
from queue import Queue
from grid2d import Grid2D

class DFS2D(Grid2D):

    def __init__(self, grid_width, grid_height, visited=None):
        Grid2D.__init__(self, grid_width, grid_height, visited)

    def dfs(self, x, y, steps=0):
        """Depth-First Search algorithm that visits every cell in a 2D grid.
        """
        if x >= self.grid_width or y >= self.grid_height:
            return
        if x < 0 or y < 0:
            return
        if self.visited[y][x]:
            return

        # Mark current cell as visited
        self.visited[y][x] = True
        self.steps_taken[y][x] = steps
        steps += 1

        # Visit every neighbouring cell
        for cell in self.neighbour(x, y):
            cellx = cell[0]
            celly = cell[1]
            self.dfs(cellx, celly, steps)

dfs = DFS2D(4, 3)
dfs.dfs(1,2)
print("Order of expansion: \n", dfs.steps_taken)

