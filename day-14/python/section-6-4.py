import numpy as np

# How to initialize np arrays when size is known
# np.arange()
increment = np.arange(1, 20, 2)
decrement = np.arange(20, 1, -3)

# np.zeros()
zeros = np.zeros(5)
multizeros = np.zeros((3, 3, 5))

# np.ones()
# np.random.random()
# np.random.randint()
# np.inspace()
# np.full()
# np.eye()
# np.title()

print("ARange Increment: {}".format(increment))
print("ARange Decrement: {}".format(decrement))
print("Zeros: \n{}".format(zeros))
print("Multidimentional Zeros: \n{}".format(multizeros))
