import numpy as np

# Compare NumPy with Standard Python Lists
list_1 = [i for i in range(1, 20, 2)]
list_2 = [i for i in range(1, 11, 1)]

sum_list = list(map(lambda x, y: x + y, list_1, list_2))
print(list_1)
print(list_2)
print(sum_list)

np_sum = np.array(list_1) + np.array(list_2)
print(np_sum)
