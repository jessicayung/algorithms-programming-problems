"""
Breadth-first Search on a 2D grid

Note: 'steps' indicates order of expansion, not distance from the source cell.

Jessica Yung
Jan 2018
"""
import numpy as np
from queue import Queue
from grid2d import Grid2D

class BFS2D(Grid2D):

    def __init__(self, grid_width, grid_height, visited=None):
        Grid2D.__init__(self, grid_width, grid_height, visited)
        self.queue = Queue()

    def bfs(self, x, y, steps=0):
        """Breadth-First Search algorithm that visits every cell in a 2D grid, where adjacent cells are defined as up to eight cells next to the current cell (can move diagonally).
        """
        if x >= self.grid_width or y >= self.grid_height:
            return
        if x < 0 or y < 0:
            return
        if self.visited[y][x]:
            return

        # Mark current cell as visited
        self.queue.put([x,y])
        self.visited[y][x] = True
        self.steps_taken[y][x] = steps
        steps += 1
        print("Visited ", x, y, "in ", steps, " steps")
        print(self.steps_taken)
        print("Visited is now")
        print(self.visited)

        # Visit every neighbouring cell
        while not self.queue.empty():
            node = self.queue.get()
            for cell in self.neighbour(node[0], node[1]):
                cellx = cell[0]
                celly = cell[1]
                # print(cell)
                if cellx < 0 or cellx >= self.grid_width:
                    continue
                if celly < 0 or celly >= self.grid_height:
                    continue
                if not self.visited[cell[1], cell[0]]:
                    self.queue.put(cell)
                    self.visited[cell[1], cell[0]] = True
                    self.steps_taken[celly, cellx] = steps
                    steps += 1

bfs = BFS2D(4, 3)
bfs.bfs(1,2)
print(bfs.steps_taken)

