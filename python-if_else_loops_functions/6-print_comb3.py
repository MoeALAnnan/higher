#!/usr/bin/python3
for x in range(0, 9):
    for y in range(x+1, 10):
        if x + y == 17:
            continue
        print(f"{x}{y}".format(x), end=", ")
print(f"89".format(x))
