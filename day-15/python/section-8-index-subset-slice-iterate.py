import numpy as np

# Section 8
# Indexing, Subsetting, Slicing and Iterating through Arrays

array_1d = np.arange(10)
print("Array: \n{}\n".format(array_1d))
print("Get Third Element(index) of the Array: {}".format(array_1d[2]))
print(
    "Get Section of (start index - end index) of the Array: {}".format(array_1d[2:5]))
print(
    "Another way: Get Section of (start index - end index) of the Array: {}".format(array_1d[[2, 3, 4]]))
