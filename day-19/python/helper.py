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


def view_1d_array(info):
    msg = "View Array Values."
    print(msg)
    print("*" * len(msg))

    strList = "First List: [{}, . . . , {}]\n".format(', '.join(map(
        str, info['listData'][0][0:5])), ', '.join(map(str, info['listData'][0][-5:])))
    strList += "Second List: [{}, . . . , {}]".format(', '.join(map(
        str, info['listData'][1][0:5])), ', '.join(map(str, info['listData'][1][-5:])))

    print(strList)


# Going to refactor these 4 functions in 1.
def perform_operations(info, action='add'):

    op = ''
    generalMsg = ''

    if action == 'add':
        op = "Addition"
        generalMsg = perform_add_operation(info)
    elif action == 'sub':
        op = "Subtraction"
        generalMsg = perform_sub_operation(info)
    elif action == 'mul':
        op = "Multiplication"
        generalMsg = perform_mul_operation(info)
    elif action == 'div':
        op = "Division"
        generalMsg = perform_divide_operation(info)

    msg = "Perform '{}' on Python Lists and on NumPy Arrays separately and then Compare their Performance".format(
        op)
    print(msg)
    print("*" * len(msg))
    print(generalMsg)


def perform_add_operation(info):
    msg = "Standard Python: \n"
    startExecution = time.time()
    perform_Ops = list(
        map(lambda x, y: (x + y), info['listData'][0], info['listData'][1]))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    msg += "Total time taken for Standard List Addition: {}\n".format(
        timeTakenForExecution)

    msg += "\nNumPy: \n"

    startExecution = time.time()
    perform_Ops = np.array(info['listData'][0]) + np.array(info['listData'][1])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Addition: {}\n".format(
        timeTakenForExecution)

    return msg


# Subtraction Operations
def perform_sub_operation(info):
    msg = "Standard Python: \n"
    startExecution = time.time()
    perform_Ops = list(
        map(lambda x, y: (y - x), info['listData'][0], info['listData'][1]))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    msg += "Total time taken for Standard List Subtraction: {}\n".format(
        timeTakenForExecution)

    msg += "\nNumPy: \n"

    startExecution = time.time()
    perform_Ops = np.array(info['listData'][1]) - np.array(info['listData'][0])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Subtraction: {}\n".format(
        timeTakenForExecution)

    return msg


def perform_mul_operation(info):  # Multiplication Operations
    msg = "Standard Python: \n"
    startExecution = time.time()
    perform_Ops = list(
        map(lambda x, y: (x * y), info['listData'][0], info['listData'][1]))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    msg += "Total time taken for Standard List Multiplication: {}\n".format(
        timeTakenForExecution)

    msg += "\nNumPy: \n"

    startExecution = time.time()
    perform_Ops = np.array(info['listData'][0]) * np.array(info['listData'][1])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Multiplication: {}\n".format(
        timeTakenForExecution)

    return msg

# Division Operations


def perform_divide_operation(info):
    msg = "Standard Python: \n"
    startExecution = time.time()
    perform_Ops = list(
        map(lambda x, y: (y / x), info['listData'][0], info['listData'][1]))
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)
    msg += "Total time taken for Standard List Division: {}\n".format(
        timeTakenForExecution)

    msg += "\nNumPy: \n"

    startExecution = time.time()
    perform_Ops = np.array(info['listData'][1]) / np.array(info['listData'][0])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Division: {}\n".format(
        timeTakenForExecution)

    return msg
