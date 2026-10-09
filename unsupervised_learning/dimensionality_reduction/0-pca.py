
#!/usr/bin/env python3
"""Perform Principal Component Analysis (PCA)."""

import numpy as np


def pca(X, var=0.95):
    """Perform PCA on a dataset.

    X is a numpy.ndarray of shape (n, d), with zero-mean features.
    var is the fraction of variance to maintain.
    Returns: W, a weight matrix of shape (d, nd).
    """
    _, S, V = np.linalg.svd(X, full_matrices=False)

    eigenvalues = S ** 2
    explained_variance = eigenvalues / np.sum(eigenvalues)
    cumulative_variance = np.cumsum(explained_variance)

    nd = np.searchsorted(cumulative_variance, var) + 1

    W = V[:nd].T

    return W