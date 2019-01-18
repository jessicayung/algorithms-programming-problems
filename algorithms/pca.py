"""
Principal Components Analysis (PCA) using NumPy

Dataset: Iris dataset.
Adapted from Plotly PCA tutorial
https://plot.ly/ipython-notebooks/principal-component-analysis/
"""

from load_data import load_iris
import numpy as np


X_std, y = load_iris(std=True)


def pca(X_std):

    # 1. Calculate covariance matrix
    mean_vec = np.mean(X_std, axis=0)
    # same as np.cov(X_std.T)
    N = X_std.shape[0]
    cov_mat = (X_std - mean_vec).T.dot((X_std - mean_vec)) / (N-1)

    # 2. Find eigenvectors and eigenvalues by SVD
    u,s,v = np.linalg.svd(X_std.T)

    eig_vals = s**2/(N-1)
    eig_vecs = u

    # Can also do by eigendecomposition -> less efficient, O(N^3) 
    # vs O(min(M,N)MN).
    # can also do for cor_mat1 = np.corrcoef(X_std.T)
    # eig_vals, eig_vecs = np.linalg.eig(cov_mat)

    # 3. Select PCs
    # Make a list of (eigenvalue, eigenvector) tuples
    eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

    # Sort the (eigenvalue, eigenvector) tuples from high to low
    eig_pairs.sort()
    eig_pairs.reverse()

    # Visually confirm that the list is correctly sorted by decreasing eigenvalues
    print('Eigenvalues and eigenectors, in descending order of eigenvalues:')
    for i in eig_pairs:
        print(i)
    return eig_pairs

eig_pairs = pca(X_std)