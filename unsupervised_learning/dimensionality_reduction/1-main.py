
#!/usr/bin/env python3
"""Test PCA v2."""

import numpy as np

pca = __import__('1-pca').pca

X = np.loadtxt("mnist2500_X.txt")
print("X:", X.shape)

T = pca(X, 50)
print("T:", T.shape)