#!/usr/bin/python

import re
from convert_polish import *

def createList(arg):
    lstLeft, lstRight, lstMiddle, lstFact, lstQuery = ([], [], [], [], [])

    for elem in arg:
        index = elem.find('=>') + 2
        if (elem.find('=>') != -1):
            elem = '+' + elem[:index] + '+' + elem[index:]
        if (re.search("^([\+|\||\^]+[!]?[(]*[!]?[A-Z]([\+|\||\^][!][A-Z])?[)]*)+[<]?=>([\+|\||\^]+[!]?[(]*[!]?[A-Z]([\+|\||\^][!][A-Z])?[)]*)+$", elem) is None):
            if (elem.find('?') == 0):
                if (re.search('^\?[A-Z]+$', elem) is None):
                    print "Wrong query: ", elem
                    exit(0)
                for char in elem:
                    if (char != '?'):
                        lstQuery.append(char)
                break
            elif (elem.find('=') == 0):
                if (elem == '='):
                    lstFact.append('=')
                elif (re.search('^\=([A-Z]+)?$', elem) is None):
                    print "Wrong fact: ", elem
                    exit(0)
                else:
                    for char in elem:
                        if (char != '='):
                            lstFact.append(char)
            else:
                print "Wrong rule: ", elem
                exit(0)
        else:
            elem = elem[1:index + 1] + elem[index + 2:]
            if (elem.find('<') != -1):
                lstLeft.append(convertPolish(elem[:elem.find('<')]))
                lstRight.append(convertPolish(elem[elem.find('>') + 1:]))
                lstMiddle.append(1)
                lstRight.append(convertPolish(elem[:elem.find('<')]))
                lstLeft.append(convertPolish(elem[elem.find('>') + 1:]))
                lstMiddle.append(1)
            else:
                lstLeft.append(convertPolish(elem[:elem.find('=')]))
                lstMiddle.append(1)
                lstRight.append(convertPolish(elem[elem.find('>') + 1:]))
    lstLeft = filter(None, lstLeft)
    lstRight = filter(None, lstRight)
    if  (not lstFact or not lstQuery):
        print "Can't find a query or a fact"
        exit(0)
    return [lstLeft, lstMiddle, lstRight, lstFact, lstQuery]


def createText(arg):
    file_object = open(arg, "r")
    toReturn = ''
    for line in file_object:
        line = line.replace(' ', '')
        if ((line.find('=') != -1 or line.find('?') != -1) and (line.find('\n') != 0) and (line.find('#') != 0)):
            if (line.find('#') == -1):
                toReturn += line
            else:
                toReturn += line[:line.find('#')] + "\n"
    toReturn = toReturn.split('\n')
    return toReturn
