import numpy as np
import time

# Section 9 - Execution speed of NumPy compared with Stanadard Python
print("Standard Python")
list1 = [i for i in range(20000000)]
list2 = [i for i in range(20000000, 40000000)]

startExecution = time.time()
perform_Ops = list(map(lambda x, y: (x * y), list1, list2))
endExecution = time.time()
timeTakenForExecution = (endExecution - startExecution)


print("Total time taken for Standard List Multiplication: {}".format(
    timeTakenForExecution))

print("\nNumPy")

list1 = np.array([i for i in range(20000000)], dtype=np.int64)
list2 = np.array([i for i in range(20000000, 40000000)], dtype=np.int64)

startExecution = time.time()
perform_Ops = list1 * list2
endExecution = time.time()
timeTakenForExecution = (endExecution - startExecution)


print("Total time taken for NumPy Multiplication: {}".format(
    timeTakenForExecution))
