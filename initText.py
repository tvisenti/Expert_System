#!/usr/bin/python

def createList(arg):
    lstLeft = []
    lstRight = []
    lstMiddle = []
    lstFact = []
    lstQuerry = []

    for elem in arg:
        if (elem.find('?') == 0):
            lstQuerry.append(elem[1:])
            break
        if (elem.find('=') == 0):
            lstFact.append(elem[1:])
        else:
            if (elem.find('<') != -1):
                lstLeft.append(elem[:elem.find('<')])
                lstMiddle.append(1)
            else:
                lstLeft.append(elem[:elem.find('=')])
                lstMiddle.append(0)
            lstRight.append(elem[elem.find('>') + 1:])
    return [lstLeft, lstMiddle, lstRight, lstFact, lstQuerry]


def createText(arg):
    file_object = open(arg, "r")
    toReturn = ""
    for line in file_object:
        line = line.replace(' ', '')
        if ((line.find('=') != -1 or line.find('?') != -1) and (line.find('\n') != 0) and (line.find('#') != 0)):
            if (line.find('#') == -1):
                toReturn += line
            else:
                toReturn += line[:line.find('#')] + "\n"
    toReturn = toReturn.split('\n')
    return toReturn
