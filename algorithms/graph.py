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
        self.visited = np.zeros(self.v)
        self.steps_taken = -1*np.ones(self.v)
        self.steps = 0

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

    def neighbour(self, vertex):
        return np.nonzero(self.adj_mat[vertex])[0]

    def dfs(self, start):
        print("at vertex", start)
        if self.visited[start]:
            print("Already visited")
            return

        print("mark as visited")
        # Mark current cell as visited
        self.visited[start] = True
        self.steps_taken[start] = self.steps
        self.steps += 1
        print(self.visited)

        # Visit every neighbouring cell
        for cell in self.neighbour(start):
            self.dfs(cell)



# Test Graph class
# t1 = Graph([[1,1,1,0],[1,1,0,0],[1,0,1,0],[0,0,0,1]], 4)
# print(t1.find_num_islands())

def test2():
    t2 = Graph(np.zeros((6,6)),6)
    edges = [[0,5],[2,4],[2,3],[3,4]]
    t2.add_edges(edges)
    print("Num islands:", t2.find_num_islands())
    print("Neighbours of vertex 0", t2.neighbour(0))
    print("Neighbours of vertex 3", t2.neighbour(3))
    t2.dfs(2)
    print(t2.steps_taken)

# test2()
