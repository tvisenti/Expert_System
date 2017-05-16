#!/usr/bin/python

import sys, re, numpy
from initText import *
from operand import *

def fillArrayQuery(query, arrayInt):
    for alpha in query[0]:
        arrayInt[ord(alpha) - 65] = 1
    return arrayInt

def main():
    if (len(sys.argv) == 2):
        file_object = createText(sys.argv[1])
        lst = createList(file_object)
        arrayInt = numpy.zeros(26)
        arrayInt = fillArrayQuery(lst[3], arrayInt)
        print (lst)
        print (arrayInt)
    elif (len(sys.argv) > 2):
        print('Too few arguments')
    else:
        print('Put one argument')

if __name__ == '__main__':
    main()
