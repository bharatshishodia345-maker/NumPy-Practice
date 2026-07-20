# finding missing value usin np.nan function

import numpy as np 

arr = np.array([1,2,np.nan,8,np.nan,6,np.nan])

print(np.isnan(arr))# nan value show True keyword