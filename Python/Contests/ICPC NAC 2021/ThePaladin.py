import sys

#########################
sys.stdin = open('TEST/TestFile.txt', 'r')
#########################


def getSubsolution(endLetter, length):
    key = (endLetter, length)
    if key in subsolutions:
        return subsolutions[key]
    listOfLinks = links[endLetter]
    bestAnswer = float("inf")
    for previousLetter, cost in listOfLinks.items():
        possibleAnswer = cost + getSubsolution(previousLetter, length-2)
        bestAnswer = min(bestAnswer, possibleAnswer)
    subsolutions[key] = bestAnswer
    return bestAnswer


nofPairs, necessaryLength = list(
    map(int, sys.stdin.readline().strip().split(' ')))

pairs = {}
letters = set()
for _ in range(nofPairs):
    edge, cost = sys.stdin.readline().strip().split(' ')
    pairs[edge] = int(cost)
    letters.add(edge[0])
    letters.add(edge[1])


subsolutions = {}
for letter in letters:
    key1 = (letter, 1)
    key2 = (letter, 2)
    subsolutions[key1] = 0
    subsolutions[key2] = float("inf")


links = {letter: {} for letter in letters}
for edge, cost in pairs.items():
    if edge[0] == edge[1]:
        key = (edge[0], 2)
        subsolutions[key] = cost
    reverse = edge[::-1]
    if reverse in pairs:
        totalCost = pairs[reverse] + pairs[edge]
        for input in [edge, reverse]:
            links[input[0]][input[1]] = totalCost

bestAnswer = float("inf")
for letter in letters:
    possibleAnswer = getSubsolution(letter, necessaryLength)
    bestAnswer = min(bestAnswer, possibleAnswer)

if bestAnswer == float("inf"):
    print(-1)
else:
    print(bestAnswer)
