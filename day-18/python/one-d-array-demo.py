# A small program to demostrate all NumPy functionalities
from helper import *

print("Welcome to NumPy 'Single Dimentional Array' Demo")

continueProgram = "Y"

while continueProgram != "X":

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

    minimum, maximum = 1, 9999998

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

        clear_screen()
        options = "Press\n"
        options += "(V) View All Informations related to this Array.\n"
        options += "(A) Add list with itself.\n"
        options += "(S) Subtract list with itself.\n"
        options += "(M) Multiply list with itself.\n"
        options += "(D) Divide list with itself.\n"
        options += "(X) to Quit to Main Menu.\n"

        interOption = (input(options).strip().upper() or 'V')[0]

        info = {
            'listSize': maxListSize,
            'listType': typeOfList,
            'seqOrRandom': sequentialOrRandom,
            'ifRandom': (minimum, maximum),
            'listData': oneDimPythonList
        }

        if interOption == "V":
            clear_screen()
            view_1d_info(info)
            dummy = input("Press any key to continue...")

        elif interOption == "A":
            clear_screen()
            print("Adding List to Itself")
            dummy = input("Press any key to continue...")

        elif interOption == "S":
            clear_screen()
            print("Subtracting List to Itself")
            dummy = input("Press any key to continue...")

        elif interOption == "M":
            clear_screen()
            print("Multiplying List to Itself")
            dummy = input("Press any key to continue...")

        elif interOption == "D":
            clear_screen()
            print("Dividing List to Itself")
            dummy = input("Press any key to continue...")

        elif interOption == "X":
            performOpOnData = 'N'
            clear_screen()

    continueProgram = (input(
        "Do you want to play with NumPy another time? Press any key to continue or (X) to terminate... ").strip().upper() or 'Y')[0]
    clear_screen()

# Program End
