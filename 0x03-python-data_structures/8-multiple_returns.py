#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    if len(sentence) == 0:
        tuple_a = 0, None
        return tuple_a
    tuple_a = len(sentence), sentence[0]
    return tuple_a
