import sys

settings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofSlots = settings[0]
costPerAd = settings[1]

incomeList = list(map(int, sys.stdin.readline().strip().split(' ')))
bestSubsolutions = [] # best income for a sequence ENDING on the specified slot

bestResult = float("-inf")
for slotNo in range(nofSlots):
    incomeForSlotAlone = incomeList[slotNo] - costPerAd
    subsolution = max(incomeForSlotAlone, incomeForSlotAlone + bestSubsolutions[slotNo - 1]) if slotNo > 0 else incomeForSlotAlone
    if bestResult < subsolution:
        bestResult = subsolution
    bestSubsolutions.append(subsolution)

print(bestResult)