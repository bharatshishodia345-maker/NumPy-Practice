"""
Program : Concatenate Arrays
Author : Bharat Thakur
"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.concatenate((arr1, arr2))

print("Concatenated Array :", new_arr)