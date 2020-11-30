import numpy as np

fromList_to_1d_Array = np.array([10, 20,  30, 40, 50])\

# Immutable tuple when converted into numpy array, it will become mutable.
fromTuple_to_1d_Array = np.array((1, 2, 3, 4, 5))

print(type(fromList_to_1d_Array))
print(fromList_to_1d_Array)

print(type(fromTuple_to_1d_Array))
print(fromTuple_to_1d_Array)
