"""
Program: Calculate Average Temperature using NumPy
Author : Bharat Thakur
"""

import numpy as np

temperatures = np.array([
    30,
    35,
    26.7,
    36,
    29,
    31.4,
    45,
    41.2,
    44.4,
    24
])

average_temperature = np.mean(temperatures)

print(f"Average Temperature = {average_temperature:.2f} °C")