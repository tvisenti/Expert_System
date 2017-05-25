#!/usr/bin/python

def convertToDigit(alpha):
    return ord(alpha) - 65

def andOpe(x, y):
    if (x == 2 or y == 2):
        return 2
    if (x == 1 and y == 1):
        return 1
    return 0

def orOpe(x, y):
    if (x == 2 and y == 2):
        return 2
    if (x == 0 and y == 0):
        return 0
    return 1

def xorOpe(x, y):
    if (x == 2 and y == 2):
        return 2
    if ((x == 1 and y == 1) or (x == 0 and y == 0)):
        return 0
    return 1

def notOpe(x):
    if (x == 2):
        return 2
    if (x == 0):
        return 1
    return 0
