import numpy as np
import time

# Section 9 - Execution speed of NumPy compared with Stanadard Python
# Point to Remember: If you initialize an arrays directly using np.array
# it will take some time.

print("Standard Python")

startExecution = time.time()
list1 = [i for i in range(2000000)]
list2 = [i for i in range(2000000, 4000000)]
perform_Ops = list(map(lambda x, y: (x * y), list1, list2))
endExecution = time.time()

timeTakenForExecution = (endExecution - startExecution)


print("Total time taken for Standard List Multiplication: {}".format(
    timeTakenForExecution))

print("\nNumPy")

startExecution = time.time()
list1 = np.array(list1, dtype=np.int64)
list2 = np.array(list2, dtype=np.int64)
perform_Ops = list1 * list2
endExecution = time.time()

timeTakenForExecution = (endExecution - startExecution)


print("Total time taken for NumPy Multiplication: {}".format(
    timeTakenForExecution))
