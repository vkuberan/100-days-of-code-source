import numpy as np

# Compare NumPy with Standard Python Lists
list_1 = [i for i in range(1, 20, 2)]
list_2 = [i for i in range(1, 20, 1)]

# If you add different size list it will add in normal Python
sum_list = list(map(lambda x, y: x + y, list_1, list_2))
print(list_1)
print(list_2)
print(sum_list)

# If you had different list sizes NumPy will trigger an error
# np_sum = np.array(list_1) + np.array(list_2)
np_sum = np.array(list_1) + np.array(list_2[:10])
print(np_sum)
