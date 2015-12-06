import re

test1 = 'turn on 0,0 through 999,999'
test2 = 'turn off 499,499 through 500,500'
test3 = 'toggle 0,0 through 999,0'

arr = [[False for i in range(1000)] for i in range(1000)]
arr2 = [[0 for i in range(1000)] for i in range(1000)]

def applyStep(command, coords1, coords2, arr):
    for i in range(coords1[0], coords2[0] + 1):
        for j in range(coords1[1], coords2[1] + 1):
            if command == 'turn off':
                arr[i][j] = False
            elif command == 'turn on':
                arr[i][j] = True
            elif command == 'toggle':
                arr[i][j] = not arr[i][j]

    return arr

def applyStep2(command, coords1, coords2, arr):
    for i in range(coords1[0], coords2[0] + 1):
        for j in range(coords1[1], coords2[1] + 1):
            if command == 'turn off' and arr[i][j] > 0:
                arr[i][j] -= 1
            elif command == 'turn on':
                arr[i][j] += 1
            elif command == 'toggle':
                arr[i][j] += 2

    return arr

def parseLine(line):
    line = line.replace('\n', '')

    command = re.sub(r' \d*,\d*', '', re.findall(r'^[\w ]*\d*,\d*', line)[0])
    coords1 = list(map(int, re.sub(r'^[\w ]* ', '', re.findall(r'^[\w ]*\d*,\d*', line)[0]).split(',')))
    coords2 = list(map(int, re.findall(r'\d*,\d*$', line)[0].split(',')))

    return (command, coords1, coords2)


def loadCommands(fname):
    commands = []

    f = open(fname)

    for line in f:
        commands.append(parseLine(line))

    return commands

def applyCommands(fname, arr, type):
    commands = loadCommands(fname)

    for command in commands:
        if type == 1:
            arr = applyStep(command[0], command[1], command[2], arr)
        else:
            arr = applyStep2(command[0], command[1], command[2], arr)

    return arr



# Tests
print(parseLine(test1))
print(parseLine(test2))
print(parseLine(test3))

arr = applyCommands('d6input.txt', arr, 1)
arr2 = applyCommands('d6input.txt', arr2, 2)

numberLit = 0

for i in arr:
    numberLit += i.count(True)

print(numberLit)

totalLit = 0

for i in arr2:
    totalLit += sum(i)

print(totalLit)
