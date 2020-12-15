# A small program to demostrate all NumPy functionalities
from helper import *

print("Welcome to NumPy 'Single Dimentional Array' Demo")

continueProgram = "Y"

while continueProgram != "X":

    maxListSize = int(
        input("Maximum List Size (Min: 25, Max: 10000000): ").strip() or "2500")

    if maxListSize <= 25:
        maxListSize = 25
    elif maxListSize >= 10000000:
        maxListSize = 10000000

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
    print("Creating Lists in Python, Pleae wait for a while....")
    oneDimPythonList = []
    oneDimPythonList2 = []
    if typeOfList == 'F' and sequentialOrRandom == 'S':
        oneDimPythonList = [float(i) for i in range(1, maxListSize)]
        oneDimPythonList2 = [float(i) for i in range(maxListSize - 1, 0, -1)]
    elif typeOfList == 'F' and sequentialOrRandom != 'S':
        oneDimPythonList = [np.round(np.random.uniform(
            minimum, maximum), 2) for i in range(1, maxListSize)]
        oneDimPythonList2 = [np.random.uniform(
            minimum, maximum) for i in range(maxListSize - 1, 0, -1)]
    elif sequentialOrRandom == 'S':
        oneDimPythonList = [i for i in range(1, maxListSize)]
        oneDimPythonList2 = [i for i in range(maxListSize - 1, 0, -1)]
    else:
        oneDimPythonList = [int(np.random.uniform(
            minimum, maximum)) for i in range(1, maxListSize)]
        oneDimPythonList2 = [int(np.random.uniform(
            minimum, maximum)) for i in range(maxListSize - 1, 0, -1)]

    performOpOnData = 'Y'

    while performOpOnData == 'Y':

        clear_screen()
        options = "Press\n"
        options += "(V) View All Informations related to this Array.\n"
        options += "(L) View Array Data.\n"
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
            'listData': (oneDimPythonList, oneDimPythonList2)
        }

        if interOption == "V":
            clear_screen()
            view_1d_info(info)
            dummy = input("Press any key to continue...")

        elif interOption == "L":
            clear_screen()
            view_1d_array(info)
            dummy = input("Press any key to continue...")

        elif interOption == "A":
            clear_screen()
            perform_operations(info, 'add')
            dummy = input("Press any key to continue...")

        elif interOption == "S":
            clear_screen()
            perform_operations(info, 'sub')
            dummy = input("Press any key to continue...")

        elif interOption == "M":
            clear_screen()
            perform_operations(info, 'mul')
            dummy = input("Press any key to continue...")

        elif interOption == "D":
            clear_screen()
            perform_operations(info, 'div')
            dummy = input("Press any key to continue...")

        elif interOption == "X":
            performOpOnData = 'N'
            clear_screen()

    continueProgram = (input(
        "Do you want to play with NumPy another time? Press any key to continue or (X) to terminate... ").strip().upper() or 'Y')[0]
    clear_screen()

# Program End
