import numpy as np

num_lst1 = [i for i in range(1, 10)]
num_lst2 = [i for i in range(10, 20)]

sum_list = list(map(lambda x, y: (x + y), num_lst1, num_lst2))

print(sum_list)
