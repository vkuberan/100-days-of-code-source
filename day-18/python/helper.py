import numpy as np
import time
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def view_1d_info(arrayProperties):
    print("View All Array Properties.")
    print("*"*30)
    print("Array Size: {}".format(arrayProperties['listSize']))
    # print("Array Value: {}".format(oneDimPythonList))
    print("Array Data Type: {}".format(
        "Float" if arrayProperties['listType'] == 'F' else "Integer"))
    print("Manual or Random: {}".format(
        "Random" if arrayProperties['seqOrRandom'] == 'R' else "Manual"))
    if arrayProperties['seqOrRandom'] == 'R':
        print("Random Minimum: {}, Random Maximum: {}".format(
            arrayProperties['ifRandom'][0], arrayProperties['ifRandom'][1]))
