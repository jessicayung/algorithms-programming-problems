"""
Articulation Points
- vertices of graphs which, when removed, will increase the number of 'islands' in the graph.
- i.e. vulnerable points of a network

Based on tutorial on HackerEarth: https://www.hackerearth.com/practice/algorithms/graphs/articulation-points-and-bridges/tutorial/

Jessica Yung
Jan 2018
"""
import numpy as np
from graph import Graph

class find_articulation_points(Graph):

    def __init__(self, adjacency_matrix, num_vertices):
        Graph.__init__(self, adjacency_matrix, num_vertices)
        self.saved_adj_mat = self.adj_mat

    def brute_force(self):
        """Alternative brute force approach: find islands using a DFS for each vertex."""
        self.articulation_points = []
        original_islands = self.find_num_islands()
        print("Original number of islands: ", original_islands)
        for vertex in range(self.v):
            self.remove_vertex(vertex)
            if self.find_num_islands() > original_islands:
                print(self.num_islands, "islands with vertex", vertex, "removed.")
                self.articulation_points.append(vertex)
            # Restore vertex
            self.v += 1
            self.adj_mat = self.saved_adj_mat
        return self.articulation_points

adjmat = np.zeros((6,6))
edges = [[0,1],[0,5],[1,2],[1,3],[2,3],[2,4],[3,4]]
test1 = find_articulation_points(adjmat, 6)
test1.add_edges(edges)
test1.brute_force()
print(test1.articulation_points)

