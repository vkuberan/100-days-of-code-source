import numpy as np
from numpy import random

# How to initialize np arrays when size is known
# np.arange()
increment = np.arange(1, 20, 2)
decrement = np.arange(20, 1, -3)

# np.zeros()
zeros = np.zeros(5)
multizeros = np.zeros((2, 2, 4))

# np.ones()
ones = np.ones(5)
multiones = np.ones((2, 2, 4))

# np.random.random(), generate random array
random = np.random.random([3, 3])

# np.random.randint()
randint = np.random.randint(1, 100, (3, 3))

# np.inspace()
# np.full()
# np.eye()
# np.title()

print("ARange Increment: {}".format(increment))
print("\n\nARange Decrement: {}".format(decrement))
print("\n\nZeros: \n{}".format(zeros))
print("\n\nMultidimentional Zeros: \n{}".format(multizeros))
print("\n\nOnes: \n{}".format(ones))
print("\n\nMultidimentional Ones: \n{}".format(multiones))
print("\n\nRandom Array: \n{}".format(random))
print("\n\nRandom Array Int: \n{}".format(randint))
