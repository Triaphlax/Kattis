import sys


def binary_search(arr, low, high, x):
    if high >= low:

        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1


while True:
    listSize = int(sys.stdin.readline())
    if listSize == 0:
        break
    listOne = []
    for i in range(0, listSize):
        listOne.append(int(sys.stdin.readline()))
    listOneSorted = listOne.copy()
    listOneSorted.sort()

    litsTwo = []
    for i in range(0, listSize):
        litsTwo.append(int(sys.stdin.readline()))
    listTwoSorted = litsTwo.copy()
    listTwoSorted.sort()

    for i in range(0, listSize):
        elementFromFirstList = listOne[i]
        indexElementInFirstSortedList = \
            binary_search(listOneSorted, 0, listSize-1, elementFromFirstList)
        correspondingElementFromSecondList = listTwoSorted[indexElementInFirstSortedList]
        print(correspondingElementFromSecondList)

    print("")
