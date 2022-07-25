import sys

def binary_search_paint_cans(arr, low, high, x):
 
    if high >= low:
 
        mid = (high + low) // 2
 
        if arr[mid] == x:
            return x
 
        elif arr[mid] > x:
            return binary_search_paint_cans(arr, low, mid - 1, x)
 
        else:
            return binary_search_paint_cans(arr, mid + 1, high, x)
 
    else:
        return arr[low]

firstInput = list(map(int, sys.stdin.readline().split(' ')))
noCanSizes = firstInput[0]
noColorsNeeded = firstInput[1]
canSizes = [] 

for canSize in range(0, noCanSizes):
    canSizes.append(int(sys.stdin.readline()))
canSizes.sort()

runningTotal = 0
for x in range(0, noColorsNeeded): 
    amountNeededFromColor = int(sys.stdin.readline())
    canSizeGotten = binary_search_paint_cans(canSizes, 0, len(canSizes)-1, amountNeededFromColor)
    runningTotal += canSizeGotten - amountNeededFromColor

print(runningTotal)