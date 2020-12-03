import numpy as np

# Section 7: Structure of Arrays
# dtype: finds data type of array.
# shape: shows shape of the array(n x m).
# itemsize: Memory used by each array element in bytes.
# ndim: Number of axes(of dimensions).

structuresOfArray = np.ones((5, 3), dtype=int)
print("Sample Array: \n{}".format(structuresOfArray))
print("Data Type: {}".format(structuresOfArray.dtype))
print("Item Size: {}".format(structuresOfArray.itemsize))
print("N Dimention: {}".format(structuresOfArray.ndim))
print("Array Shape: {}".format(structuresOfArray.shape))

# Creating a 3-D array. Difficult to print it.
# reshape() simply reshape a 1-D array.
