"""
Program : NumPy Type Conversion
Author  : Bharat Thakur
"""

import numpy as np

arr = np.array([1.6, 5.2, 8.4, 6.3, 5, 8, 9.4])

print("Original Data Type :", arr.dtype)

new_arr = arr.astype(int)

print("Converted Array :", new_arr)
print("New Data Type :", new_arr.dtype)