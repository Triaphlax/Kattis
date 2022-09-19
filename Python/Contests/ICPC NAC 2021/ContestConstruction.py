import sys

###############
sys.stdin = open('TEST/TestFile.txt', 'r')
###############


def binary_search_contest_construction(arr, low, high, x):

    if high >= low:
        mid = (high + low) // 2

        if arr[mid] == x:
            if not mid >= len(arr) and arr[mid] == x:
                mid = mid + 1
            return mid - 1

        elif arr[mid] < x:
            return binary_search_contest_construction(arr, low, mid - 1, x)

        else:
            return binary_search_contest_construction(arr, mid + 1, high, x)

    else:
        return high


def getSubSolution(first, second, left):
    key = (first, second, left)
    if key in subsolutions:
        return subsolutions[key]
    firstValue = totalQuestionsList[first]
    secondValue = totalQuestionsList[second]
    minimumThirdValue = firstValue - secondValue
    subarray = totalQuestionsList[second+1:]
    endIndex = binary_search_contest_construction(
        subarray, 0, len(subarray)-1, minimumThirdValue)
    if endIndex == -1:
        subsolutions[key] = 0
        return 0
    nextIndices = range(second+1, second+(endIndex+1)+1)

    answer = 0
    if left == 1:
        answer = len(nextIndices)
    else:
        for third in nextIndices:
            answer += getSubSolution(second, third, left-1)
    subsolutions[key] = answer
    return answer


nofTotalQuestions, nofFinalQuestions = list(
    map(int, sys.stdin.readline().strip().split(' ')))

totalQuestionsList = []
for _ in range(nofTotalQuestions):
    totalQuestionsList.append(int(sys.stdin.readline().strip()))

totalQuestionsList.sort(reverse=True)

subsolutions = {}

starts = [(index1, index2) for index1 in range(nofTotalQuestions)
          for index2 in range(index1+1, nofTotalQuestions)]

totalAnswer = 0
for start in starts:
    totalAnswer += getSubSolution(start[0], start[1], nofFinalQuestions - 2)

print(totalAnswer)
