import numpy as np

prices = np.array([100, 200, 300, 400])

discount = 10  # Discount Percentage

final_price = prices - (prices * discount / 100)

print("Original Prices :", prices)
print("Final Prices    :", final_price)