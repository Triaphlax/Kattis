import sys

######################
sys.stdin = open('TEST/TestFile.txt', 'r')
######################

lines = sys.stdin.readlines()

for line in lines:
    settings = list(map(int, line.strip().split(' ')))
    nofStones = settings[0]
    nofOptions = settings[1]
    optionsList = []
    for i in range(nofOptions):
        optionsList.append(settings[2 + i])

    resultDict = {0: -1, 1: 1}
    for subsolutionStones in range(2, nofStones+1):
        bestResult = -1
        for option in optionsList:
            if option > subsolutionStones:
                continue
            else:
                currentResult = -1 * resultDict[subsolutionStones - option]
                if currentResult == 1:
                    bestResult = 1
                    break
        resultDict[subsolutionStones] = bestResult

    finalResult = resultDict[nofStones]
    if finalResult == 1:
        print("Stan wins")
    else:
        print("Ollie wins")
