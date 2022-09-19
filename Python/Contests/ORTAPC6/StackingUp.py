import sys
from unittest import result


def getOffsetFromNumber(number):
    binRep = "{0:b}".format(number)
    extraOffset = 0
    ones = 0
    for index in range(-1, (-1 * len(binRep)) - 1, -1):
        val = binRep[index]
        if val == '1':
            ones += 1
            extraOffset += abs(index + 1)
    return extraOffset + (ones - 1)


######################
sys.stdin = open('TEST/TestFile.txt', 'r')
######################

stackSize = int(sys.stdin.readline().strip())
resultStack = list(map(int, sys.stdin.readline().strip().split(' ')))

# check duplicates
dActions = 0
lastElement = resultStack[-1]
for i in range(stackSize-2, -1, -1):
    nextElement = resultStack[i]
    if nextElement == lastElement:
        dActions += 1
    else:
        break

# do the others
offset = 0
onePlusList = []

for i in range(stackSize-dActions-1, -1, -1):
    element = resultStack[i]
    necessaryOutcome = element + offset
    extraOffset = getOffsetFromNumber(necessaryOutcome)
    offset += extraOffset
    onePlusList = [necessaryOutcome] + onePlusList

resultString = ""
for entry in onePlusList:
    if entry == '1':
        print('1', end='')
        continue
    binRep = "{0:b}".format(entry)
    ones = 0
    for index in range(-1, (-1 * len(binRep)) - 1, -1):
        val = binRep[index]
        if val == '1':
            ones += 1
            times = abs(index + 1)
            print('11+', end='')
            print('d' * times, end='')
            print('+' * times, end='')
    
    # print('1', end='')
    # maxes = (entry - 1) // sys.maxsize
    # remainder = (entry - 1) % sys.maxsize
    # for max in range(maxes):
    #     print("1+" * (sys.maxsize), end='')
    # print("1+" * remainder, end='')

print('d' * dActions, end='')
