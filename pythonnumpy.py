import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

arr_zeros = np.zeros((3, 4))  # 3x4 array of zeros
print(arr_zeros)

arr_ones = np.ones((2, 3))  # 2x3 array of ones
print(arr_ones)

arr_range = np.arange(0, 10, 2)  # array from 0 to 10 with a step of 2
print(arr_range)

arr_linspace = np.linspace(0, 10, 5)  # 5 values from 0 to 10
print(arr_linspace)