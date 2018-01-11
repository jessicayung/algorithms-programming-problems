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

    def is_adjacent(self, v1, v2):
        return self.adj_mat[v1, v2]

    def remove_vertex(self, v):
        self.adj_mat = np.delete(self.adj_mat, v, 0)
        self.adj_mat = np.delete(self.adj_mat, v, 1)
        self.v -= 1

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

    def add_edges(self, edges):
        """Edges = an array of length-two arrays, each length-two array representing an edge."""
        for edge in edges:
            i = edge[0]
            j = edge[1]
            self.adj_mat[i][j] = self.adj_mat[j][i] = 1



# Test Graph class
# t1 = Graph([[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,0,0,1]], 4)
# print(t1.find_num_islands())

# t2 = Graph(np.zeros((6,6)),6)
# edges = [[0,5],[2,4],[2,3],[3,4]]
# t2.add_edges(edges)
# print(t2.find_num_islands())
