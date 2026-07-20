# find the finate value

import numpy as np

arr = np.array([1, np.inf, 5, 8, np.inf])

print("Original Array :", arr)
print("Infinite Values:", np.isinf(arr))