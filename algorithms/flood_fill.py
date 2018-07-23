"""
Flood Fill

Jessica Yung
Jan 2018
"""
import numpy as np

class FloodFill2D:

    def __init__(self, grid_width, grid_height, visited=None):
        self.grid_width = grid_width
        self.grid_height = grid_height
        if visited is None:
            self.visited = np.zeros((grid_height, grid_width))
        else:
            self.visited = visited
        self.steps_taken = np.zeros((grid_height, grid_width))


    def flood_fill(self, x, y, steps=0):
        """Basic flood fill algorithm that visits every cell in a 2D grid, where adjacent cells are defined as up to eight cells next to the current cell (can move diagonally).
        DFS-based implementation.
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
        print("Visited ", x, y, "in ", steps, " steps")
        print(self.steps_taken)
        print("Visited is now")
        print(self.visited)

        # Visit every neighbouring cell
        for cell in self.neighbour(x, y):
            self.flood_fill(cell[0], cell[1], steps+1)

    def neighbour(self, x, y):
        neighbours = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                neighbours.append([x + dx, y + dy])
        return neighbours

ff = FloodFill2D(4, 3)
ff.flood_fill(1,2)
print(ff.steps_taken)

