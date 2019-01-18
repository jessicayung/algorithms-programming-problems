"""
K-means implementation

Seems okay: Have not tested this rigorously, but this separates 'Iris-setosa' 
pretty well from 'Iris-versicolor' and 'Iris-virginica',
but mixes the latter two. 

Dataset: Iris dataset.
"""

from load_data import load_iris
import numpy as np


X_std, y = load_iris(std=True)


def k_means(X, num_means=3, num_iterations=10):
    """K means. Assumes each datapoint is a 1D array."""
    # data dim
    N, D = X.shape
    
    # initialise vars
    assignments = np.zeros(N)
    dists = np.zeros((N, num_means))    

    # 1. Init means
    means = np.random.random((num_means, D))
    
    # 2. Iterate
    for i in range(num_iterations):
        # 2a(i) Calculate dists
        for k in range(num_means):
            dists[:,k] = np.sum((X - np.tile(means[k],(N,1)))**2,axis=1)

        # 2a(ii): Assign clusters
        for n in range(N):
            assignments[n] = np.argmin(dists[n])

        # 2b. Recalculate cluster means
        for k in range(num_means):
            means[k] = np.mean([X[i] for i in range(N) if assignments[i] == k], axis=0)

    return means, assignments


means, assignments = k_means(X_std)

print(assignments, y)