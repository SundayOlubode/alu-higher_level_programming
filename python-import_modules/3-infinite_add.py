#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    Sum = 0
    if len(argv) < 1:
        Sum = 0
    else:
        for i in argv[1:]:
            Sum += int(i)
    print('{}'.format(Sum))
