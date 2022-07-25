import sys


def removeWeightsUnderBar(row, barWeight):
    return [weight for weight in row if weight > barWeight]


def checkIfValidForRow(row):
    if len(row) % 2 == 1:
        return False
    for index in range(0, len(row), 2):
        if row[index] is not row[index+1]:
            return False
    return True


def binary_search_free_weights(arr, low, high):
 
    if high >= low:
 
        weightIndex = (high + low) // 2

        possibleWhenLiftingThisWeight = \
            checkIfValidForRow(removeWeightsUnderBar(firstRow, arr[weightIndex])) \
                and checkIfValidForRow(removeWeightsUnderBar(secondRow, arr[weightIndex]))
 
        if possibleWhenLiftingThisWeight:
            return binary_search_free_weights(arr, low, weightIndex - 1)
 
        else:
            return binary_search_free_weights(arr, weightIndex + 1, high)

    else:
        return arr[low]


dumbbellsPerRow = int(sys.stdin.readline())

firstRow = list(map(int, sys.stdin.readline().strip().split(' ')))
secondRow = list(map(int, sys.stdin.readline().strip().split(' ')))

combinedRows = []
combinedRows.extend(firstRow)
combinedRows.extend(secondRow)
combinedRows.sort()

allWeights = []
for index in range(0, len(combinedRows), 2):
    allWeights.append(combinedRows[index])

if checkIfValidForRow(firstRow) and checkIfValidForRow(secondRow):
    print(0)
else:
    result = binary_search_free_weights(allWeights, 0, len(allWeights)-1)
    print(result)
