#!/usr/bin/python3

def andOpe(x, y):
    if (x == 1 and y == 1):
        return 1
    return 0

def orOpe(x, y):
    if (x == 0 and y == 0):
        return 0
    return 1

def xorOpe(x, y):
    if ((x == 1 and y == 1) or (x == 0 and y == 0)):
        return 0
    return 1

def notOpe(x):
    if (x == 0):
        return 1
    return 0
