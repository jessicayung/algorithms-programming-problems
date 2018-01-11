"""
Graph class

Jessica Yung
Jan 2018
"""
import numpy as np

class Graph:
    def __init__(self, adjacency_matrix, num_vertices):
        self.adj_mat = adjacency_matrix
        self.v = num_vertices

    def is_adjacent(v1, v2):
        return self.adj_mat[v1, v2]

    def remove_vertex(v):
        self.adj_mat[v,:] = 0
        self.adj_mat[:,v] = 0

    def find_num_islands(self):
        num_islands = 0
        accounted_for = np.zeros(self.v)
        for v in range(self.v):
            if accounted_for[v]:
                continue
            if not sum(self.adj_mat[v] * accounted_for):
                num_islands += 1
            # accounted_for[v] = True
            indices = np.nonzero(self.adj_mat[v][v:])[0] # need [0] bc else returns a tuple
            indices += v
            for index in indices:
                accounted_for[index] = True
        self.num_islands = num_islands
        return num_islands

# Test Graph class
# t1 = Graph([[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,0,0,1]], 4)
# print(t1.find_num_islands())

