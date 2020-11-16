import numpy as np
import time

# sizeof the array
sizeOfArray = 1000000

# Typical Python List
A1 = range(sizeOfArray)
A2 = range(sizeOfArray)

# Numpy Array
a1 = np.arange(sizeOfArray)
a2 = np.arange(sizeOfArray)

# Adding two python lists
start = time.time()
result = [(x + y) for x, y in zip(A1, A2)]
print("Adding two Python list took :", (time.time() - start) * 1000)


# Adding Numpy Array
start = time.time()
result = a1 + a2
print("numpy array took :", (time.time() - start)*1000)
