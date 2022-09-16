import sys

################
sys.stdin = open('TEST/TestFile.txt', 'r')
################

alice1, alice2 = list(map(int, sys.stdin.readline().strip().split(' ')))
layout = sys.stdin.readline().strip()

# 0 - alice1
# alice1 - alice2
# alice2 - 10

setSizes = [alice1 - 1, (alice2 - alice1) - 1, (10 - alice2) - 1]

setBob1 = -1
setBob2 = -1
currentSet = 0
for i in range(4):
    letter = layout[i]
    if letter == 'A':
        currentSet += 1
    if letter == 'B' and setBob1 == -1:
        setBob1 = currentSet
    if letter == 'B' and setBob1 > -1:
        setBob2 = currentSet

if setBob1 == setBob2:
    if setSizes[setBob1] == 2:
        if setBob1 == 0:
            print(str(alice1 - 2) + ' ' + str(alice1 - 1))
        if setBob1 == 1:
            print(str(alice2 - 2) + ' ' + str(alice2 - 1))
        if setBob1 == 2:
            print(str(alice2 + 1) + ' ' + str(alice2 + 2))
    else:
        print(str(-1))
elif setSizes[setBob1] == 1 and setSizes[setBob2] == 1:
    resultString = ""
    if setBob1 == 0:
        resultString += str(alice1 - 1)
    elif setBob1 == 1:
        resultString += str(alice2 - 1)
    resultString += " "
    if setBob2 == 1:
        resultString += str(alice2 - 1)
    elif setBob2 == 2:
        resultString += str(alice2 + 1)
    print(resultString)
else:
    print(str(-1))
