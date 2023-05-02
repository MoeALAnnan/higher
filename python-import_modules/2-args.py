#!/usr/bin/python3
import sys
argv = sys.argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print(f"1 argument: \n1: {argv[1]}")
    elif len(argv) >= 2:
        x = len(argv) - 1
        print(f"{x} arguments:")
        for i in range(len(argv) - 1):
            print(f"{i + 1}: {argv[i + 1]}")
