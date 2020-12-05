import numpy as np
import time

print("Welcome to NumPy 'Single Dimentional Array' Demo")

continueProgram = "Y"

while continueProgram != "N":

    try:

        minimum, maximum = map(int, input(
            "Range of the list (minimum, maximum): ").strip().split(",")) or 1, 10
        typeOfList = input(
            "Date Type of list: F float or any key for Integer: ").strip() or 'I'
        manualOrRandom = input(
            "Generate List Data: any key for Random or M for manual: ").strip() or 'R'

        if minimum <= 0 or maximum <= 0:
            minimum, maximum = 1, 10
        elif minimum >= maximum:
            minimum, maximum = maximum, minimum

    except:
        minimum, maximum = 1, 10

    print("minimum: {}, maximum: {}".format(minimum, maximum))
    print("List Data Type: {}".format(typeOfList))
    print("Manual or Random: {}".format(manualOrRandom))

    continueProgram = input(
        "Any key to continue or N(o) to terminimumate... ").strip().upper()

print("End of Program.")
