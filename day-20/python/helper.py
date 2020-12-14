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
    retValue = ''

    if action == 'add':
        op = "Addition"
        retValue = perform_add_operation(info)
    elif action == 'sub':
        op = "Subtraction"
        retValue = perform_sub_operation(info)
    elif action == 'mul':
        op = "Multiplication"
        retValue = perform_mul_operation(info)
    elif action == 'div':
        op = "Division"
        retValue = perform_divide_operation(info)

    msg = "Perform '{}' on Python Lists and on NumPy Arrays separately and then Compare their Performance".format(
        op)
    print(msg)
    print("*" * len(msg))
    print(retValue[0])

    doYouWantToContinue = (input(
        "Do you want to display values of the Performed Action? Y(es) to display or any key to quit...").strip().upper() or 'Q')[0]

    if doYouWantToContinue == 'Y':
        print_data(op, info, retValue)


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
    perform_Ops_NumPy = np.array(
        info['listData'][0]) + np.array(info['listData'][1])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Addition: {}\n".format(
        timeTakenForExecution)

    return [msg, perform_Ops, perform_Ops_NumPy]


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
    perform_Ops_NumPy = np.array(
        info['listData'][1]) - np.array(info['listData'][0])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Subtraction: {}\n".format(
        timeTakenForExecution)

    return [msg, perform_Ops, perform_Ops_NumPy]


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
    perform_Ops_NumPy = np.array(
        info['listData'][0]) * np.array(info['listData'][1])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Multiplication: {}\n".format(
        timeTakenForExecution)

    return [msg, perform_Ops, perform_Ops_NumPy]

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
    perform_Ops_NumPy = np.array(
        info['listData'][1]) / np.array(info['listData'][0])
    endExecution = time.time()
    timeTakenForExecution = (endExecution - startExecution)

    msg += "Total time taken for NumPy Division: {}\n".format(
        timeTakenForExecution)

    return [msg, perform_Ops, perform_Ops_NumPy]


def print_data(op, data, returndata):
    clear_screen()
    tmp = op + " Results (500 rows per page)\n"
    op = tmp + "*" * len(tmp)

    pageLen = 500
    totalPages = round(len(data['listData'][0]) / pageLen)

    header = "{:61s} {:16s} {:<51s}".format(
        'Python List', ' ', 'NumPy Array')
    astrickStr = '*' * len(header)

    for i in range(1, (totalPages + 1), 1):
        start, end = 1, pageLen
        if i == 1:
            start = 1
            end = pageLen
            if end >= len(data['listData'][0]):
                end = len(data['listData'][0])
        else:
            start = ((i - 1) * pageLen) + 1
            end = i * pageLen
            if end >= len(data['listData'][0]):
                end = len(data['listData'][0])

        start, end = (start - 1), (end - 1)

        clear_screen()
        print("Page {} of {}".format(i, totalPages))
        print(header)
        print(astrickStr)
        for iCnt in range(start, end):
            counterString = str(iCnt + 1) + ")"
            fmtStr1 = "{:<10s} {:<12d} {:<8s} {:<12d} {:<5s} {:<15d}".format(counterString,
                                                                             data['listData'][0][iCnt], 'x',
                                                                             data['listData'][1][iCnt], '=',
                                                                             (data['listData'][0][iCnt] * data['listData'][1][iCnt]))

            fmtStr2 = "{:<12d} {:<8s} {:<12d} {:<5s} {:<15d}".format(
                data['listData'][0][iCnt], 'x', data['listData'][1][iCnt], '=', (data['listData'][0][iCnt] * data['listData'][1][iCnt]))

            print("{} {:>5s}{:<5s} {}".format(fmtStr1, ' ', '|', fmtStr2))

        print("\n")
        print(astrickStr)
        print("Page {} of {}".format(i, totalPages))
        print(header)
        print(astrickStr)
        processQuit = (input(
            "Press any key to continue or Q to quit...").strip().upper() or 'Y')[0]

        if processQuit == 'Q':
            break
