import sys

######################
sys.stdin = open('TEST/TestFile.txt', 'r')
######################


def get_subsolution(stones):
    if stones in subsolutions:
        return subsolutions[stones]
    if stones < 1:
        return False
    for move in optionsList:
        resultingStones = stones - move
        isWin = get_subsolution(resultingStones)
        if not isWin:
            subsolutions[stones] = True
            return True
    subsolutions[stones] = False
    return False


lines = sys.stdin.readlines()

for line in lines:
    x = sys.getrecursionlimit()
    settings = list(map(int, line.strip().split(' ')))
    nofStones = settings[0]
    nofOptions = settings[1]
    optionsList = []
    for i in range(nofOptions):
        optionsList.append(settings[2 + i])
    optionsList.sort(reverse=True)

    subsolutions = {1: True}
    result = get_subsolution(nofStones)

    if result:
        print("Stan wins")
    else:
        print("Ollie wins")
