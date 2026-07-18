"""
Program :  vertical staking and horigantal staking in NumPy
Author : Bharat Thakur
Repository : NumPy-Practice
"""
import numpy as np 
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1, arr2)),"vertical staking")
print(np.hstack((arr1, arr2)),"horigantal staking")