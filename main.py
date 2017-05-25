#!/usr/bin/python

import sys, re
from initText import *
from solve import *

def main():
    if (len(sys.argv) == 2):
        file_object = createText(sys.argv[1])
        lst = createList(file_object)
        arrayInt = [0] * 26
        arrayInt = fillArrayQuery(lst[3], arrayInt)
        handlerArg(lst, arrayInt)
        displaySolution(lst[4], arrayInt)

    elif (len(sys.argv) > 2):
        print('Too few arguments')
    else:
        print('Put one argument')

if __name__ == '__main__':
    main()
