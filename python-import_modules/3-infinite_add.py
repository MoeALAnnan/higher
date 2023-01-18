#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    y = 0
    if (len(argv) > 1):
        for x in range(1, len(argv)):
            y = y + int(argv[x])
        print("{}".format(y))
    else:
        print("0")
