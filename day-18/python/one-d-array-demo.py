# A small program to demostrate all NumPy functionalities
from helper import *

print("Welcome to NumPy 'Single Dimentional Array' Demo")

continueProgram = "Y"

while continueProgram != "N":

    maxListSize = int(
        input("Maximum List Size (Min: 25, Max: 1000000): ").strip() or "25")

    if maxListSize <= 25:
        maxListSize = 25
    elif maxListSize >= 1000000:
        maxListSize = 1000000

    typeOfList = input(
        "Date Type of list: F for float or any key for Integer: ").strip().upper() or 'I'
    manualOrRandom = input(
        "Generate List Data: M for manual or any key for Random: ").strip().upper() or 'R'

    if manualOrRandom == 'R':

        try:
            # minimum, maximum = map(int, input(
            #     "Range of the list (minimum, maximum): ").strip().split(","))
            minimum, maximum = [int(x) for x in input(
                "Range of the list (minimum, maximum): ").strip().split(",")[0:2]]

            if minimum <= 0 or maximum <= 0:
                minimum, maximum = 1, 9999998
            if minimum >= 9999999:
                minimum = 1
            if maximum >= 9999999:
                maximum = 9999998
            if minimum >= maximum:
                minimum, maximum = maximum, minimum

        except:
            minimum, maximum = 1, 9999998

    # 1-d Python List
    oneDimPythonList = []
    if typeOfList == 'F':
        oneDimPythonList = [float(i) for i in range(1, maxListSize)]
    else:
        oneDimPythonList = [i for i in range(1, maxListSize)]

    # 1-d NumPy Array

    print("Array Size: {}".format(maxListSize))
    print("Array Value: {}".format(oneDimPythonList))
    print("Array Data Type: {}".format(
        "Float" if typeOfList == 'F' else "Integer"))
    print("Manual or Random: {}".format(
        "Random" if manualOrRandom == 'R' else "Manual"))
    if manualOrRandom == 'R':
        print("Random Minimum: {}, Random Maximum: {}".format(minimum, maximum))

    continueProgram = input(
        "N(o) to terminate or Any key to continue... ").strip().upper()
    clear_screen()

# Program End
