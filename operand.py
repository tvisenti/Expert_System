#!/usr/bin/python

def convertToDigit(alpha):
    return ord(alpha) - 65

def handlerArg(lst, arrayInt):
    i = 0
    valLeft = 0
    while (i < len(lst[0])):
        elemLeft = lst[0][i]
        elemMiddle = lst[1][i]
        elemRight = lst[2][i]
        if (len(elemLeft) <= 2):
            if (elemLeft[0] == '!'):
                valLeft = notOpe(arrayInt[convertToDigit(elemLeft[1])])
                arrayInt = assignToArray(elemRight, arrayInt, valLeft)
            else:
                valLeft = arrayInt[convertToDigit(elemLeft)]
                arrayInt = assignToArray(elemRight, arrayInt, valLeft)
        else:
            createArray(elemLeft, arrayInt, elemRight)
        i += 1

def solveNotOpe(elem, arrayInt):
    if (elem >= 0 and elem <= 2):
        val = elem
    elif (elem[0] == '!'):
        val = notOpe(arrayInt[convertToDigit(elem[1])])
    else:
        val = arrayInt[convertToDigit(elem[0])]
    return val

def solveOpe(elemLeft, elemRight, arrayInt, case):
    valLeft = solveNotOpe(elemLeft, arrayInt)
    valRight = solveNotOpe(elemRight, arrayInt)
    if (case == "add"):
        return andOpe(valLeft, valRight)
    elif (case == "or"):
        return orOpe(valLeft, valRight)
    elif (case == "xor"):
        return xorOpe(valLeft, valRight)


def switchOperator(tab, arrayInt, elemRight):
    nb = 0
    val = -1
    while (nb < len(tab)):
        if (nb % 2 != 0):
            if (tab[nb] == '+'):
                if (val != -1):
                    val = solveOpe(val, tab[nb + 1], arrayInt, "add")
                else:
                    val = solveOpe(tab[nb - 1], tab[nb + 1], arrayInt, "add")
            elif (tab[nb] == '|'):
                if (val != -1):
                    val = solveOpe(val, tab[nb + 1], arrayInt, "or")
                else:
                    val = solveOpe(tab[nb - 1], tab[nb + 1], arrayInt, "or")
            elif (tab[nb] == '^'):
                if (val != -1):
                    val = solveOpe(val, tab[nb + 1], arrayInt, "xor")
                else:
                    val = solveOpe(tab[nb - 1], tab[nb + 1], arrayInt, "xor")
        nb += 1
    if (elemRight[0] == '!'):
        val = notOpe(val)
        arrayInt[convertToDigit(elemRight[1])] = val
    else:
        arrayInt[convertToDigit(elemRight)] = val

def createArray(elem, arrayInt, elemRight):
    if (elem.find('(') == -1):
        i = 0
        j = 0
        tab = [''] * len(elem) # enleve le ! avec un -
        while (j < len(elem)):
            if (elem[j] == '+' or elem[j] == '|' or elem[j] == '^'):
                i += 1
                tab[i] += elem[j]
                i += 1
            else:
                tab[i] += elem[j]
            j += 1
    else:
        print("je rentre")
        # Gere les parantheses
    print (tab)
    switchOperator(tab, arrayInt, elemRight)
    return

def assignToArray(char, arrayInt, val):
    arrayInt[convertToDigit(char)] = arrayInt[val]
    return arrayInt

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
