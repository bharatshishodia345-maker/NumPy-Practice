"""
Program : Insert Row in 2D Array
Author : Bharat Thakur
"""

import numpy as np

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original Array")
print(arr)

new_arr = np.insert(arr, 2, [7, 8, 9], axis=0)

print("\nUpdated Array")
print(new_arr)