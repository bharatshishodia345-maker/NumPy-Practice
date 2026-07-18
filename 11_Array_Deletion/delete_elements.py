
"""
Program :  delete element usnig delete function in NumPy
Author : Bharat Thakur
Repository : NumPy-Practice
"""

import numpy as np 

arr_1 = np.array([1,2,3,4,5,6])
arr_2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

new_arr_1 = np.delete(arr_1, 2)# delete function is work delete element throw index number
new_arr_2 = np.delete(arr_2, 0, axis=0)
print(arr_1,"orignal array")
print(new_arr_1)
print("Delete 2 index of number")
print(arr_2,"orignal array")

print(new_arr_2)# delete index 0 row 

print("delete 0 index of row")