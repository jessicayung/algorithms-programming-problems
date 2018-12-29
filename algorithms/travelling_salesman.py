"""
Travelling Salesman Problem:
An Exact Dynamic Programming Solution in Python

Jessica Yung
Dec 2018
"""
import numpy as np

class TravellingSalesman:

    def __init__(self, graph, start=0):
        """Initialise with graph and node you start from.
        :param graph: takes the form of an adjacency matrix
                      (suitable since we are given a fully connected graph).
        :param start: an int (index in adj matrix).
        Node you start from doesn't make a difference since this is a tour.
        """
        self.graph = graph
        self.start = start
        self.nodes = list(np.arange(len(graph)))
        self.cost_dict = {}

    def cost(self, nodes, end):
        if (tuple(nodes), end) in self.cost_dict.keys():
            return self.cost_dict[(tuple(nodes), end)]
        else:
            self.cost_dict[tuple(nodes), end] = self.calc_cost(nodes, end)
            return self.cost_dict[tuple(nodes), end]

    def calc_cost(self, nodes, end):
        if end not in nodes:
            return Exception("Endpoint not in nodes to visit.")
        # print("Nodes: {}".format(nodes))
        if len(nodes) == 1:
            return 0
        if len(nodes) == 2:
            return self.graph[nodes[0], nodes[1]]
        non_end_nodes = nodes.copy()
        non_end_nodes.remove(end)
        temp = [self.cost(non_end_nodes, j) + self.graph[j, end] for j in non_end_nodes if j != self.start]
        # print("Non end nodes: {}".format(non_end_nodes))
        # print("End: ", end)
        # for j in non_end_nodes:
        #     if j != self.start:
        #         print(self.cost(non_end_nodes, j))
        #         print(self.graph[j, end])
        #         print("Graph: ", self.graph)
        #         print("j={}, end={}".format(j, end))
        # print("cost candidates:", temp)
        return min(temp)

    def dp(self):
        """Dynamic programming solution to Travelling Salesman problem."""
        # calculate costs
        return min(self.cost(self.nodes, i) + self.graph[i, 0] for i in self.nodes[1:])
        # return self.cost(self.nodes, self.start)


# test case:
def create_adj_matrix(distances):
    """dists: (n-1)x(n-1) matrix with (n-1)*n/2 entries
    dists from 0 to 1, 2,...n-1, then dists from 1 to 2,...,n-1, up to dists from n-1.
    cells that don't represent dists in input may not exist or can exist but are ignored.
    """
    n = len(distances) + 1
    mat = np.diag(np.ones(n)*np.inf)
    for i in range(n-1):
        for j in range(n-i-1):
            mat[i, j+i+1] = mat[j+i+1, i] = distances[i][j]
    return mat

dists = create_adj_matrix([[4, 3],[2]])
# print(dists)
ts = TravellingSalesman(dists, 0)
soln = ts.dp()
print("Min dist:", soln)
# print(ts.cost_dict)
