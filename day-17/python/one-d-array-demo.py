# A small program to demostrate some of the basic NumPy functionalities
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
            minimum, maximum = map(int, input(
                "Range of the list (minimum, maximum): ").strip().split(","))

            if minimum <= 0 or maximum <= 0:
                minimum, maximum = 1, 10
            elif minimum >= maximum:
                minimum, maximum = maximum, minimum

        except:
            minimum, maximum = 1, 10

    print("List Size: {}".format(maxListSize))
    print("List Data Type: {}".format(typeOfList))
    print("Manual or Random: {}".format(manualOrRandom))
    if manualOrRandom == 'R':
        print("minimum: {}, maximum: {}".format(minimum, maximum))

    continueProgram = input(
        "Any key to continue or N(o) to terminimumate... ").strip().upper()
    clear_screen()

print("End of Program.")
