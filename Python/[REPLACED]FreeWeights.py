from enum import Enum
import sys


class Status(Enum):
    Undecided = 1
    NeedsToBePickedUp = 2
    DoesNotNeedToBePickedUp = 3


def UpdateDictDuring(forDumbbellWeight):
    for weight in dumbbellStatuses.keys():
        if dumbbellStatuses[weight] == Status.Undecided and forDumbbellWeight > weight:
            dumbbellStatuses[weight] = Status.NeedsToBePickedUp
        if forDumbbellWeight in dumbbellStatuses:
            if forDumbbellWeight < weight and dumbbellStatuses[weight] == Status.Undecided:
                dumbbellStatuses[forDumbbellWeight] = Status.NeedsToBePickedUp


def UpdateDictEnd():
    for key, value in dumbbellStatuses.items():
        if value == Status.Undecided:
            dumbbellStatuses[key] = Status.NeedsToBePickedUp

dumbbellsPerRow = int(sys.stdin.readline())
largestWeightToBeMoved = 0

for rowNo in [0,1]:
    row = list(map(int, sys.stdin.readline().strip().split(' ')))
    dumbbellStatuses = {}
    for currentDumbbellIndex in range(0, dumbbellsPerRow):
        currentDumbbell = row[currentDumbbellIndex]
        UpdateDictDuring(currentDumbbell)
        if currentDumbbell not in dumbbellStatuses:
            dumbbellStatuses[currentDumbbell] = Status.Undecided
        elif dumbbellStatuses[currentDumbbell] is Status.Undecided:
            dumbbellStatuses[currentDumbbell] = Status.DoesNotNeedToBePickedUp

    UpdateDictEnd()

    x = 3
    
    for weight in dumbbellStatuses.keys():
        if dumbbellStatuses[weight] == Status.NeedsToBePickedUp and largestWeightToBeMoved < weight:
            largestWeightToBeMoved = weight

print(largestWeightToBeMoved)