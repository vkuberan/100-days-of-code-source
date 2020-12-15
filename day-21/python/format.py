import random
# Formatting strings and numbers in python
print("%d %s cost $%.2f" % (120, 'bananas', 12.9800))
print("{0:<10d} x {1:>10d} = {2:>20d}".format(100, 100, 10000))


for i in range(10000, 10101, 1):

    if i == 10000:
        header = "{:51s} {:5s} {:<51s}".format(
            'Python List', ' ', 'NumPy Array')
        astrickStr = '*' * len(header)
        print(header)
        print(astrickStr)

    multiplied1 = random.randint(10, 1000000)
    fmtStr1 = "{:<12d} {:<3s} {:<12d} {:<5s} {:<15d}".format(
        multiplied1, 'x', i, '=', (i * multiplied1))

    multiplied2 = random.randint(10, 1000000)
    fmtStr2 = "{:<12d} {:<3s} {:<12d} {:<5s} {}".format(
        multiplied2, 'x', i, '=', (i * multiplied2))
    print("{} {:<5s} {}".format(fmtStr1, '|', fmtStr2))
