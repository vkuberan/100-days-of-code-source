import random
import platform
import subprocess


def clear_screen():
    command = "cls" if platform.system().lower() == "windows" else "clear"
    return subprocess.call(command, shell=True)


def squared(numbers):
    return list(map(lambda x: (x*x), numbers))


def cubed(numbers):
    return list(map(lambda x: (x*x*x), numbers))


def sort_min_to_max(numbers):
    return sorted(numbers)


def high_order_func_demo(transform, numbers):
    return transform(numbers)


options = 'S'

while options != 'X':
    clear_screen()
    options = (
        input("S to squared (default), C to cubed and B to sort or X to quit: ").strip().upper() or 'S')[0]

    if options == 'X':
        break

    try:
        numbers = list(map(int, input(
            "Enter Numbers Seperated by Comma (Ex: 1, 2, 3, 4): ").strip().split(",")))
        print("\n")
    except:
        numbers = [i if i % 2 == 0 else -
                   (random.randint(1, 99999999)) for i in range(1, 11)]

    print("\n")

    msg = "Original List: "
    print(msg)
    print('*' * len(msg))
    print(numbers)
    print("\n")

    if options == 'S':
        msg = ("Hight Order Function Called: 'squared'")
        print(msg)
        print('*' * len(msg))
        print(high_order_func_demo(squared, numbers))
    elif options == 'C':
        msg = ("Hight Order Function Called: 'cubed'")
        print(msg)
        print('*' * len(msg))
        print(high_order_func_demo(cubed, numbers))
    elif options == 'B':
        msg = (
            "Hight Order Function Called: 'sort_min_to_max' (Sort the list Min to Max)")
        print(msg)
        print('*' * len(msg))
        print(high_order_func_demo(sort_min_to_max, numbers))

    input("\nPress any key to continue....")
