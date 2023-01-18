#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_1 = dir(hidden_4)
    for x in list_1:
        if x[0] != '_':
            print(x)
