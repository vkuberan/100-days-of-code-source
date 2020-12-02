import numpy as np

# Different kind of actions that you can perform on np array
np_array_1 = np.array([i for i in range(1, 20, 2)])
np_array_2 = np.array([i for i in range(1, 20, 1)])


# Get values based on conditions
np_array_3 = np_array_2 >= 10

print(np_array_1)
print(np_array_2)
print(np_array_3)

np_array_3_cond = np_array_2[np_array_3]

print(np_array_3_cond)
