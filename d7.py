import operator
import re

def apply1ParamBitOp(operation, x, bitspace = 65536):
    if x > 0:
        return operation(int(x)) % bitspace
    else:
        return 0

def apply2ParamBitOp(operation, x, y, bitspace = 65536):
    if x > 0 and y > 0:
        return operation(int(x), int(y)) % bitspace
    else:
        return 0

def parseLine(line, wireArray, lines):
    tokens = line.split(' ')

    if tokens[1] == '->':
        # assignment
        val = 0

        if bool(re.match(r'\d', tokens[0])):
            val = int(tokens[0])
        else:
            try:
                val = int(wireArray[tokens[0]])
            except KeyError:
                return (wireArray, lines)

        wireArray[tokens[2]] = val

    elif tokens[2] == '->':
        # NOT
        val = 0

        if bool(re.match(r'\d', tokens[1])):
            val = int(tokens[1])
        else:
            try:
                val = int(wireArray[tokens[1]])
            except KeyError:
                return (wireArray, lines)

        wireArray[tokens[3]] = apply1ParamBitOp(operator.inv, val)

    elif tokens[3] == '->':
        # AND, OR, bit shifts, etc
        num1 = 0
        num2 = 0
        op = None

        if bool(re.match(r'\d', tokens[0])):
            num1 = int(tokens[0])
        else:
            try:
                num1 = int(wireArray[tokens[0]])
            except KeyError:
                return (wireArray, lines)

        if bool(re.match(r'\d', tokens[2])):
            num2 = int(tokens[2])
        else:
            try:
                num2 = int(wireArray[tokens[2]])
            except KeyError:
                return (wireArray, lines)

        if tokens[1] == 'AND':
            op = operator.and_
        elif tokens[1] == 'OR':
            op = operator.or_
        elif tokens[1] == 'LSHIFT':
            op = operator.lshift
        elif tokens[1] == 'RSHIFT':
            op = operator.rshift

        wireArray[tokens[4]] = apply2ParamBitOp(op, num1, num2)

    del lines[lines.index(line)]
    return (wireArray, lines)

def runFile(fname):
    arr = {}

    f = open(fname)

    while len(list(f)) > 0:
        for line in f:
            (arr, f) = parseLine(line.replace('\n', ''), arr, f)

    return arr


print(parseLine('123 -> x', {}, ['123 -> x']))
print(parseLine('y -> x', { 'y' : 5 }, ['y -> x']))
print(parseLine('NOT 456 -> x', { 'y' : 456 }, ['NOT 456 -> x']))
print(parseLine('NOT y -> x', { 'y' : 456 }, ['NOT y -> x']))
print(parseLine('x AND y -> d', { 'x' : 123, 'y' : 456 }, ['x AND y -> d']))

arr = runFile('d7input.txt')

print(arr)
