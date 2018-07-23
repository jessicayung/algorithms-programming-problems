import numpy as np

class Grid2D:

    def __init__(self, grid_width, grid_height, visited=None):
        self.grid_width = grid_width
        self.grid_height = grid_height
        if visited is None:
            self.visited = np.zeros((grid_height, grid_width))
        else:
            self.visited = visited
        self.steps_taken = np.zeros((grid_height, grid_width))

    def neighbour(self, x, y):
        neighbours = []
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                neighbours.append([x + dx, y + dy])
        return neighbours