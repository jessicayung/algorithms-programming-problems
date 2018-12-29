"""
Travelling Salesman Problem:
An Exact Dynamic Programming Solution in Python

Jessica Yung
Dec 2018
"""

class TravellingSalesman:

    def __init__(self, graph, start):
        """Initialise with graph and node you start from.
        :param graph: takes the form of an adjacency matrix
                      (suitable since we are given a fully connected graph).
        :param start: an int (index in adj matrix).
        Node you start from doesn't make a difference since this is a tour.
        """
        self.graph = graph
        self.start = start
        self.nodes = np.arange(len(graph))

    def cost(self, nodes, end):
        if (nodes, end) is in self.cost_dict.keys():
            return self.cost_dict[(nodes, end)]
        else:
            self.cost_dict[nodes, end] = self.calc_cost(nodes, end)
            return self.cost_dict[nodes, end]

    def calc_cost(self, nodes, end):
        if end not in nodes:
            return Exception("Endpoint not in nodes to visit.")
        if len(nodes) == 1:
            return 0
        if len(nodes) == 2:
            return self.graph[nodes[0], nodes[1]]
        non_end_nodes = nodes.copy().remove(end)
        return min(self.cost(non_end_nodes, j) + self.graph[j, end] for j in non_end_nodes if j != self.start)

    def dp(self):
        """Dynamic programming solution to Travelling Salesman problem."""
        return self.cost(self.nodes, self.start)


# test case:
def create_adj_matrix(dists):
    """dists: (n-1)x(n-1) matrix with (n-1)*n/2 entries
    dists from 0 to 1, 2,...n-1, then dists from 1 to 2,...,n-1.
    cells that don't represent dists are left as zeroes.
    """
    pass

