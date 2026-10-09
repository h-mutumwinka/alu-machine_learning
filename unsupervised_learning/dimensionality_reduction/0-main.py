
#!/usr/bin/env python3
"""Test the PCA function."""

import numpy as np
pca = __import__('0-pca').pca

np.random.seed(0)
a = np.random.normal(size=50)
b = np.random.normal(size=50)
c = np.random.normal(size=50)

X = np.array([a, b, c, 2 * a, -5 * b, 10 * c]).T
X_m = X - np.mean(X, axis=0)

W = pca(X_m)
T = np.matmul(X_m, W)
X_t = np.matmul(T, W.T)

print("W shape:", W.shape)
print("Transformed data shape:", T.shape)
print("Reconstruction error:", np.sum((X_m - X_t) ** 2) / X_m.shape[0])