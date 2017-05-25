#!/usr/bin/python

from operand import *
from color import *

def displaySolution(solve, arrayInt):
    for char in solve:
        if (arrayInt[convertToDigit(char)] == 0):
            print ('\033[93m' + char + ' is false' + '\033[91m')
        elif (arrayInt[convertToDigit(char)] == 1):
            print ('\033[92m' + char + ' is true')
        else:
            print ('\033[95m' + char + ' is ambiguous')

def fillArrayQuery(query, arrayInt):
    if (query[0] == '='):
        return arrayInt
    for alpha in query:
        arrayInt[ord(alpha) - 65] = 1
    return arrayInt

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

def npi(expr, arrayInt):
    pile = []
    ifNot = 0
    for elt in expr:
        if ifNot == 1:
            pile.append(notOpe(arrayInt[convertToDigit(elt)]))
            ifNot = 0
        elif elt == '+':
            b, a = pile.pop(), pile.pop()
            pile.append(solveOpe(a, b, arrayInt, "add"))
        elif elt == '|':
            b, a = pile.pop(), pile.pop()
            pile.append(solveOpe(a, b, arrayInt, "or"))
        elif elt == '^':
            b, a = pile.pop(), pile.pop()
            pile.append(solveOpe(a, b, arrayInt, "xor"))
        elif elt == '!':
            ifNot = 1
        else:
            pile.append(arrayInt[convertToDigit(elt)])
    return pile.pop()

def createArray(elem, arrayInt):
    i = 0
    j = 0
    tab = [''] * len(elem)
    while (j < len(elem)):
        if (elem[j] == '+' or elem[j] == '|' or elem[j] == '^'):
            i += 1
            tab[i] += elem[j]
            i += 1
        else:
            tab[i] += elem[j]
        j += 1
    return tab

def assignToArray(char, arrayInt, val):
    arrayInt[convertToDigit(char)] = val
    return arrayInt

def handlerPlus(val, string, elemRight, iniFact, arrayInt):
    ifNot = 0
    if (val == 1):
        for char in elemRight:
            if (char == '!'):
                ifNot = 1
            if (char == '+' or char == '|' or char == '^' or char == '!'):
                continue
            else:
                if (char in iniFact and ifNot == 1):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
                else:
                    arrayInt[convertToDigit(char)] = 1
    elif (val == 0):
        for char in elemRight:
            if (char == '!'):
                ifNot = 1
            if (char == '+' or char == '|' or char == '^' or char == '!'):
                continue
            else:
                if (char in iniFact and ifNot == 1):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
    return arrayInt

def handlerOr(val, string, elemRight, iniFact, arrayInt):
    ifNot = 0
    if (val == 1):
        for char in elemRight:
            if (char == '!'):
                ifNot = 1
            if (char == '+' or char == '|' or char == '^' or char == '!'):
                continue
            else:
                if (char in iniFact and ifNot == 1):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
                else:
                    if ((arrayInt[convertToDigit(string[0])] == 0 or arrayInt[convertToDigit(string[0])] == 2) and arrayInt[convertToDigit(string[1])] == 0):
                        arrayInt[convertToDigit(char)] = 2
                    elif (arrayInt[convertToDigit(string[0])] == 1 and arrayInt[convertToDigit(string[1])] == 0):
                        arrayInt[convertToDigit(string[1])] = 2
                    elif (arrayInt[convertToDigit(string[0])] == 0 and arrayInt[convertToDigit(string[1])] == 1):
                        arrayInt[convertToDigit(string[0])] = 2
                    elif (arrayInt[convertToDigit(string[0])] == 0):
                        arrayInt[convertToDigit(string[1])] = 1
    elif (val == 0):
        for char in elemRight:
            if (char == '!'):
                ifNot = 1
            if (char == '+' or char == '|' or char == '^' or char == '!'):
                continue
            else:
                if (char in iniFact and ifNot == 1):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
                else:
                    if (arrayInt[convertToDigit(string[0])] == 1 or arrayInt[convertToDigit(string[1])] == 1):
                        print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                        exit (1)
    return arrayInt

def handlerXor(val, string, elemRight, iniFact, arrayInt):
    ifNot = 0
    if (val == 1):
        for char in elemRight:
            if (char == '!'):
                ifNot = 1
            if (char == '+' or char == '|' or char == '^' or char == '!'):
                continue
            else:
                if (char in iniFact and ifNot == 1):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
                elif ((arrayInt[convertToDigit(string[0])] == 1) and (arrayInt[convertToDigit(string[1])] == 1)):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
                else:
                    if (((arrayInt[convertToDigit(string[0])] == 0) or (arrayInt[convertToDigit(string[0])] == 2)) and (arrayInt[convertToDigit(string[1])] == 0)):
                        arrayInt[convertToDigit(char)] = 2
                    elif (arrayInt[convertToDigit(string[1])] == 0):
                        if (char == string[0]):
                            arrayInt[convertToDigit(char)] = 1
                        else:
                            arrayInt[convertToDigit(char)] = 0
                    elif (arrayInt[convertToDigit(string[0])] == 0):
                        if (char == string[1]):
                            arrayInt[convertToDigit(char)] = 1
                        else:
                            arrayInt[convertToDigit(char)] = 0
    elif (val == 0):
        for char in elemRight:
            if (char == '!'):
                ifNot = 1
            if (char == '+' or char == '|' or char == '^' or char == '!'):
                continue
            else:
                if (char in iniFact and ifNot == 1):
                    print "\033[91m", "Rules Error: fact '" + char + "' was set to true and then false!"
                    exit (1)
                else:
                    if (arrayInt[convertToDigit(string[0])] == 0 and arrayInt[convertToDigit(string[1])] == 1):
                            arrayInt[convertToDigit(char)] = 1
                    elif (arrayInt[convertToDigit(string[0])] == 1 and arrayInt[convertToDigit(string[1])] == 0):
                            arrayInt[convertToDigit(char)] = 1
    return arrayInt

def doubleAssignToArray(val, elemRight, arrayInt, iniFact):
    i = 0
    string = retNewStringFromLst(elemRight)
    if (val == 2):
        arrayInt = changeValueToAmbiguous(string, arrayInt)
    if (elemRight.find('+') != -1):
        arrayInt = handlerPlus(val, string, elemRight, iniFact, arrayInt)
    elif (elemRight.find('|') != -1):
        arrayInt = handlerOr(val, string, elemRight, iniFact, arrayInt)
    elif (elemRight.find('^') != -1):
        arrayInt = handlerXor(val, string, elemRight, iniFact, arrayInt)
    return arrayInt

def changeValueToAmbiguous(string, arrayInt):
    for char in string:
        arrayInt[convertToDigit(char)] = 2
    return arrayInt

def retNewStringFromLst(elemRight):
    string = ''
    i = 0
    while (i < len(elemRight)):
        if (elemRight[i] >= 'A' and elemRight[i] <= 'Z'):
            string += elemRight[i]
        i += 1
    return string

def retNewLstMultipleFact(toRet, elemRight):
    for char in elemRight:
        if (char >= 'A' and char <= 'Z'):
            toRet.insert(0, char)
    return toRet

def searchInList(lstFact, lstLeft, lstRight, arrayInt, iniFact):
    i = 0
    toRet = []
    val = 0
    while (i < len(lstLeft)):
        if (lstLeft[i].find(lstFact[0]) != -1):
            curChar = lstLeft[i]
            tab = createArray(curChar, arrayInt)
            val = npi(lstLeft[i], arrayInt)
            if (lstRight[i].find('+') == -1 and lstRight[i].find('|') == -1 and lstRight[i].find('^') == -1):
                if (lstRight[i].find('!') != -1):
                    arrayInt = assignToArray(lstRight[i][1], arrayInt, notOpe(val))
                    toRet.insert(0, lstRight[i][1])

                else:
                    arrayInt = assignToArray(lstRight[i], arrayInt, val)
                    toRet.insert(0, lstRight[i])
            else:
                arrayInt = doubleAssignToArray(val, lstRight[i], arrayInt, iniFact)
                toRet = retNewLstMultipleFact(toRet, lstRight[i])
        i += 1
    return toRet

def handlerArg(lst, arrayInt):
    valLeft = 0
    toBreak = lst[4]
    if (lst[3][0] == '='):
        lstFact = lst[4][:]
    else:
        lstFact = lst[3][:]
    while (len(lstFact) != 0):
        elemLeft = lst[0]
        elemRight = lst[2]
        if (lst[3][0] == '='):
            tabChars = searchInList(lstFact, elemLeft, elemRight, arrayInt, lst[4])
        else:
            tabChars = searchInList(lstFact, elemLeft, elemRight, arrayInt, lst[3])
        if (not tabChars):
            lstFact.pop(0)
        if (toBreak == tabChars and tabChars):
            break
        else:
            toBreak = tabChars
        popFlag = 0
        for char in tabChars:
            if char in lstFact:
                continue
            elif popFlag == 1:
                lstFact.insert(0, char)
            else:
                popFlag = 1
                lstFact.pop(0)
                lstFact.insert(0, char)
        if ((tabChars == toBreak and lst[3][0] == '=' and lstFact) or (lstFact == lst[3])):
            lstFact.pop(0)
