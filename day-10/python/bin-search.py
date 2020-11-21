# Binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.


def bin_search(arr, l, r, x):

    if r >= l:

        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bin_search(arr, l, mid-1, x)
        else:
            return bin_search(arr, mid + 1, r, x)

    else:
        return -1


tempText = input("Enter numbers with space: ").strip().split()
numberToFind = int(input("Enter the Number to find: ").strip().split()[0])
binArray = sorted([int(i) for i in tempText])

result = bin_search(binArray, 0, len(binArray) - 1, numberToFind)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")
