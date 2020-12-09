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
    sequentialOrRandom = input(
        "Generate List Data: S for sequential or any key for Random: ").strip().upper() or 'R'

    if sequentialOrRandom == 'R':

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
    if typeOfList == 'F' and sequentialOrRandom == 'S':
        oneDimPythonList = [float(i) for i in range(1, maxListSize)]
    elif typeOfList == 'F' and sequentialOrRandom != 'S':
        oneDimPythonList = [np.random.uniform(
            minimum, maximum) for i in range(1, maxListSize)]
    elif sequentialOrRandom == 'S':
        oneDimPythonList = [i for i in range(1, maxListSize)]
    else:
        oneDimPythonList = [int(np.random.uniform(
            minimum, maximum)) for i in range(1, maxListSize)]

    performOpOnData = 'Y'

    while performOpOnData == 'Y':

        options = "Press\n"
        options += "(D) to Display All Informations.\n"
        options += "(A) Add list with itself.\n"
        options += "(S) Subtract list with itself.\n"
        options += "(M) Multiply list with itself.\n"
        options += "(D) Divide list with itself.\n"
        options += "(X) to Quit to Main Menu.\n"

        interOption = (input(options).strip().upper() or 'D')[0]

        if interOption == "D":
            print("Display all Informations related to Array.")
            dummy = input("Press any key to continue...")
            clear_screen()

        elif interOption == "A":
            print("Adding List to Itself")
            dummy = input("Press any key to continue...")
            clear_screen()

        elif interOption == "S":
            print("Subtracting List to Itself")
            dummy = input("Press any key to continue...")
            clear_screen()

        elif interOption == "M":
            print("Multiplying List to Itself")
            dummy = input("Press any key to continue...")
            clear_screen()

        elif interOption == "D":
            print("Dividing List to Itself")
            dummy = input("Press any key to continue...")
            clear_screen()

        elif interOption == "X":
            performOpOnData = 'N'

        # 1-d NumPy Array

    # print("Array Size: {}".format(maxListSize))
    # print("Array Value: {}".format(oneDimPythonList))
    # print("Array Data Type: {}".format(
    #     "Float" if typeOfList == 'F' else "Integer"))
    # print("Manual or Random: {}".format(
    #     "Random" if sequentialOrRandom == 'R' else "Manual"))
    # if sequentialOrRandom == 'R':
    #     print("Random Minimum: {}, Random Maximum: {}".format(minimum, maximum))

    continueProgram = input(
        "N(o) to terminate or Any key to continue... ").strip().upper()
    clear_screen()

# Program End
