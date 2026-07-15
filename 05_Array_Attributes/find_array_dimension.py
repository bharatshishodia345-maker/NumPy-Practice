"""
Program : Find the Dimension of NumPy Arrays
Author  : Bharat Thakur
"""

import numpy as np

# One-Dimensional Array
array_1d = np.array([1, 5, 9])

# Two-Dimensional Array
array_2d = np.array([
    [1, 5, 9],
    [9, 5, 1]
])

# Three-Dimensional Array
array_3d = np.array([
    [
        [1, 5, 9],
        [7, 5, 3],
        [8, 5, 2]
    ]
])

print("1D Array Dimension:", array_1d.ndim)
print("2D Array Dimension:", array_2d.ndim)
print("3D Array Dimension:", array_3d.ndim)