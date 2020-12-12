import numpy as np
import time
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def view_1d_info(arrayProperties):
    msg = "View All Array Properties."
    print(msg)
    print("*" * len(msg))
    print("Array Size: {}".format(arrayProperties['listSize']))
    # print("Array Value: {}".format(oneDimPythonList))
    print("Array Data Type: {}".format(
        "Float" if arrayProperties['listType'] == 'F' else "Integer"))
    print("Sequential or Random: {}".format(
        "Random" if arrayProperties['seqOrRandom'] == 'R' else "Sequential"))
    if arrayProperties['seqOrRandom'] == 'R':
        print("Random Minimum: {}, Random Maximum: {}".format(
            arrayProperties['ifRandom'][0], arrayProperties['ifRandom'][1]))


def view_1d_array(oneDimList):
    msg = "View Array Values."
    print(msg)
    print("*" * len(msg))
    print(oneDimList)


# Add Operations
def perform_add_operation(info):
    msg = "Add Lists and then with NumPy Array separately and then Compare their Performance. \n"
    print(msg)
    print("*" * len(msg))

    print("Standard Python: ")
    startExecution = time.time()
    perform_Ops = list(map(lambda x: (x + x), info['listData']))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    print("Total time taken for Standard List Addition: {}".format(
        timeTakenForExecution))

    print("\nNumPy: ")

    startExecution = time.time()
    list1 = np.array(info['listData'])
    perform_Ops = list1 + list1
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    print("Total time taken for NumPy Addition: {}".format(
        timeTakenForExecution))


# Subtraction Operations
def perform_sub_operation(info):
    msg = "Subtract Lists and then with NumPy Array sepatetely and then Compare their Performance."
    print(msg)
    print("*" * len(msg))
    print("Standard Python: ")
    startExecution = time.time()
    perform_Ops = list(map(lambda x: (x - x), info['listData']))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    print("Total time taken for Standard List Subtraction: {}".format(
        timeTakenForExecution))

    print("\nNumPy: ")

    startExecution = time.time()
    list1 = np.array(info['listData'])
    perform_Ops = list1 - list1
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    print("Total time taken for NumPy Subtraction: {}".format(
        timeTakenForExecution))


def perform_mul_operation(info):  # Multiplication Operations
    msg = "Multiply Lists and then with NumPy Array sepatetely and then Compare their Performance."
    print(msg)
    print("*" * len(msg))
    print("Standard Python: ")
    startExecution = time.time()
    perform_Ops = list(map(lambda x: (x * x), info['listData']))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    print("Total time taken for Standard List Multiplication: {}".format(
        timeTakenForExecution))

    print("\nNumPy: ")

    startExecution = time.time()
    list1 = np.array(info['listData'])
    perform_Ops = list1 * list1
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    print("Total time taken for NumPy Multiplication: {}".format(
        timeTakenForExecution))


# Division Operations
def perform_divide_operation(info):
    msg = "Divide Lists and then with NumPy Array sepatetely and then Compare their Performance."
    print(msg)
    print("*" * len(msg))
    print("Standard Python: ")
    startExecution = time.time()
    perform_Ops = list(map(lambda x: (x / x), info['listData']))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    print("Total time taken for Standard List Division: {}".format(
        timeTakenForExecution))

    print("\nNumPy: ")

    startExecution = time.time()
    list1 = np.array(info['listData'])
    perform_Ops = list1 / list1
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    print("Total time taken for NumPy Division: {}".format(
        timeTakenForExecution))
