# fill the finate value

import numpy as np

arr = np.array([1, np.inf, 5, 8, -np.inf])

clean_arr = np.nan_to_num(arr, posinf=100, neginf=-100)

print("Original Array :", arr)
print("Modified Array :", clean_arr)