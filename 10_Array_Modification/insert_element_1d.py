"""
Program : Insert Element in 1D Array
Author : Bharat Thakur
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print("Original Array :", arr)

new_arr = np.insert(arr, 1, 15)

print("Updated Array :", new_arr)