# A small program to demostrate all NumPy functionalities
from helper import *

print("Welcome to NumPy 'Single Dimentional Array' Demo")

continueProgram = "Y"

while continueProgram != "N":

    maxListSize = int(input("Maximum List Size: ").strip() or "25")
    typeOfList = input(
        "Date Type of list: F float or any key for Integer: ").strip() or 'I'
    manualOrRandom = input(
        "Generate List Data: any key for Random or M for manual: ").strip() or 'R'

    if manualOrRandom == 'R':

        try:
            # minimum, maximum = map(int, input(
            #     "Range of the list (minimum, maximum): ").strip().split(","))
            minimum, maximum = [int(x) for x in input(
                "Range of the list (minimum, maximum): ").strip().split(",")[0:2]]

            if minimum <= 0 or maximum <= 0:
                minimum, maximum = 1, 100000
            elif minimum >= maximum:
                minimum, maximum = maximum, minimum

        except:
            minimum, maximum = 1, 100000

    print("Array Size: {}".format(maxListSize))
    print("Array Data Type: {}".format(
        "Float" if typeOfList == 'F' else "Integer"))
    print("Manual or Random: {}".format(
        "Random" if manualOrRandom == 'R' else "Manual"))
    if manualOrRandom == 'R':
        print("Random Minimum: {}, Random Maximum: {}".format(minimum, maximum))

    continueProgram = input(
        "Any key to continue or N(o) to terminate... ").strip().upper()
    clear_screen()

print("End of Program.")
