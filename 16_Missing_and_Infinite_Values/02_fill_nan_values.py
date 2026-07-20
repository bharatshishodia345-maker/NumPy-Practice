# Filing nan value

import numpy as np

arr = np.array([1, 2, np.nan, 8, np.nan, 6, np.nan])

clean_arr = np.nan_to_num(arr)

print("Original Array :", arr)
print("Clean Array    :", clean_arr)