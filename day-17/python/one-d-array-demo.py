import numpy as np
import time

print("Welcome to NumPy 'Single Dimentional Array' Demo")

continueProgram = "Y"

while continueProgram == "Y":
    try:
        min, max = input(
            "Enter Minimum, Maximum value for the list Ex: (10, 20): ").strip().split(",")
        if min <= 0 or max <= 0:
            min, max = 1, 10
        if min >= max:
            min, max = (max - 1), min
    except:
        min, max = 1, 10

    print("Min: {}, Max: {}".format(min, max))

    continueProgram = input(
        "Y(es) to continue or any key to terminate... ").strip().upper()

print("End of Program.")
