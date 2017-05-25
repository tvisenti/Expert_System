postfix = []
temp = []
operator = -10
operand = -20
leftparentheses = -30
rightparentheses = -40
none = -50
empty = -60


def precedence(s):
    if s is '(':
        return 0
    elif s is '|':
        return 1
    elif s is '+':
        return 2
    else:
        return 99

def typeof(s):
    if s is '(':
        return leftparentheses
    elif s is ')':
        return rightparentheses
    elif s is '+' or s is '|' or s is '^':
        return operator
    elif s is '!':
        return none
    elif s is ' ':
        return empty
    else :
        return operand

def convertPolish(infix):
    cptLeftParentheses = 0
    cptRightParentheses = 0
    del postfix[:]
    for i in infix :
        type = typeof(i)
        if type is leftparentheses:
            cptLeftParentheses += 1
            temp.append(i)
        elif type is rightparentheses:
            cptRightParentheses += 1
            if (not temp):
                print "Error parentheses"
                exit (1)
            next = temp.pop()
            while next is not '(':
                postfix.append(next)
                next = temp.pop()
        elif type is operand:
            postfix.append(i)
        elif type is operator:
            p = precedence(i)
            while len(temp) is not 0 and p <= precedence(temp[-1]):
                postfix.append(temp.pop())
            temp.append(i)
        elif type is none:
            postfix.append(i)
        elif type is empty:
            continue
    while len(temp) > 0 :
        postfix.append(temp.pop())
    if (cptRightParentheses != cptLeftParentheses):
        print "Error parentheses"
        exit (1)
    return ''.join(postfix)
