#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is not None:
        if len(sentence) == 0:
            x = 0,
            y = None
        else:
            x = len(sentence)
            y = sentence[0]
        return (x, y,)
