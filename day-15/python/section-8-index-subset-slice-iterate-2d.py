import numpy as np

# Section 8
# 2 Dimentional array: Indexing, Subsetting, Slicing and Iterating through Arrays

array_2d = np.array([np.arange(1, 10), np.arange(11, 20), np.arange(21, 30)])
print("Array: \n{}\n".format(array_2d))
print("Get Column using Simple Indexing(row, column): {}".format(
    array_2d[2, 5]))
print("Get Entire Row using index array_2d[1] or array_2d[1, :]: {}".format(
    array_2d[1]))
print("Get Entire Column using index array_2d[:, 1]: {}".format(
    array_2d[:, 1]))
