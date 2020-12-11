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


def perform_add_operation(info):
    msg = "Add Lists and then with NumPy Array separately and then Compare their Performance."
    print(msg)
    print("*" * len(msg))


def perform_sub_operation(info):
    msg = "Subtract Lists and then with NumPy Array sepatetely and then Compare their Performance."
    print(msg)
    print("*" * len(msg))


def perform_mul_operation(info):
    msg = "Multiply Lists and then with NumPy Array sepatetely and then Compare their Performance."
    print(msg)
    print("*" * len(msg))


def perform_divide_operation(info):
    msg = "Divide Lists and then with NumPy Array sepatetely and then Compare their Performance."
    print(msg)
    print("*" * len(msg))
