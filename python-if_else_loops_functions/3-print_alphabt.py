#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if x in [101, 113]:
        continue
    print(f"{chr(x)}".format(x), end="")
