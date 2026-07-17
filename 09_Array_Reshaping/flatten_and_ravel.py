# multi deminisonal array convert into 1D array

import numpy as np 

arr = np.array([[1,2,3],[4,5,6]])

print("is the 2D array")
print(arr)
print("convert Array",arr.ravel())
print("copy reval Array",arr.flatten())
