import sys

settings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofItems = settings[0]
maxCost = settings[1]

itemsList = list(map(int, sys.stdin.readline().strip().split(' ')))
itemsList.sort()

currentCutOff = maxCost
currentIndex = 0
itemsInPromotion = 0
while True:
    nextItemCost = itemsList[currentIndex]
    if nextItemCost <= currentCutOff:
        itemsInPromotion += 1
        currentCutOff = maxCost - nextItemCost
    else:
        break  
    currentIndex += 1
    if currentIndex == nofItems:
        break

if itemsInPromotion == 0 and nofItems > 0:
    itemsInPromotion = 1

print(itemsInPromotion)