# convert the given number to binary if it is even or
# hexadecimal if it is not


def evens_and_odds(n):
    if n % 2 == 0:
        return bin(n).replace("0b", "")
    else:
        return hex(n).replace("0x", "")


num = int(input("Enter an Integer Number: ").strip())
print(evens_and_odds(num))
