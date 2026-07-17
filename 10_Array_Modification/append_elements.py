"""
Program : Append Elements in NumPy
Author : Bharat Thakur
Repository : NumPy-Practice
"""

import numpy as np

arr = np.array([10, 20, 30])

print("Original Array :", arr)

new_arr = np.append(arr, [40, 50, 60])

print("After Append :", new_arr)