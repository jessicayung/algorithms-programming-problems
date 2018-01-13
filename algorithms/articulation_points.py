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
        self.backedges = np.zeros(num_vertices)
        self.potential_articulation_points = [[] for i in range(num_vertices)]
        self.articulation_points = []
        # self.min_discovery_time = np.full(num_vertices, num_vertices)

    def brute_force(self):
        """Alternative brute force approach: find islands using a DFS for each vertex."""
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

    def back_edge(self, start):
        """ Back edge method of finding articulation points.

        Back edge: an edge that connects a node to an ancestor of its parent.

        Claim: If a vertex u has a child v and none of the vertices in the v-subtree have a back edge to ANY vertex discovered before u (this works bc data structure is a tree), u is an articulation point.
        - i.e. if u is removed, then the v-subtree will be disconnected from the graph.
        """
        # print("at vertex", start)
        if self.visited[start]:
            # print("Already visited")
            return

        # print("mark as visited")
        # Mark current cell as visited
        self.visited[start] = True
        self.steps_taken[start] = self.steps
        self.steps += 1
        # print(self.visited)

        # Visit every neighbouring cell
        for cell in self.neighbour(start):
            if self.steps_taken[start] > self.steps_taken[cell]:
                self.backedges[start] += 1
                self.potential_articulation_points[start].append(cell)
            self.back_edge(cell)
        if self.backedges[start] == 1:
            ap = self.potential_articulation_points[start][0]
            if ap not in self.articulation_points:
                self.articulation_points.append(ap)


def test1():
    adjmat = np.zeros((6,6))
    edges = [[0,1],[0,5],[1,2],[1,3],[2,3],[2,4],[3,4]]
    test1 = find_articulation_points(adjmat, 6)
    test1.add_edges(edges)
    test1.back_edge(1)
    # test1.brute_force()
    print("Articulation points:", test1.articulation_points)

test1()
