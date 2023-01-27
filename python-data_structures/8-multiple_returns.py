#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        new_tup = ()
        x = len(sentence)
        y = sentence[0]
        new_tup = x, y
        return (new_tup)
