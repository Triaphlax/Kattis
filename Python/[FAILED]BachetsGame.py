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

    resultDict = [False, True]
    for subsolutionStones in range(2, nofStones+1):
        bestResult = False
        for option in optionsList:
            if option > subsolutionStones:
                continue
            else:
                currentResult = not resultDict[subsolutionStones - option]
                if currentResult:
                    bestResult = True
                    break
        resultDict.append(bestResult)

    finalResult = resultDict[nofStones]
    if finalResult:
        print("Stan wins")
    else:
        print("Ollie wins")
