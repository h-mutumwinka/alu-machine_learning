
#!/usr/bin/env python3
"""Perform PCA dimensionality reduction."""

import numpy as np


def pca(X, ndim):
    """Reduce the dimensions of a dataset using PCA.

    X is a numpy.ndarray of shape (n, d).
    ndim is the number of dimensions to retain.
    Returns: T, the transformed dataset of shape (n, ndim).
    """
    X_centered = X - np.mean(X, axis=0)

    _, _, V = np.linalg.svd(X_centered, full_matrices=False)

    W = V[:ndim].T

    T = np.matmul(X_centered, W)

    return T