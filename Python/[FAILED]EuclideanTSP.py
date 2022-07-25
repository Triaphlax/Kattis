import sys
import math


def EuclideanTSP(c):
    operationsNeededForCalculation = (n * math.pow(math.log2(n), c * math.sqrt(2))) / (p * 1000000000)
    timeNeededForCalculation = operationsNeededForCalculation # / (p * 1000000000)
    approximationFactor = (1 + (1/c))
    timeNeededForTravel = (s/v)*approximationFactor
    totalTime = timeNeededForCalculation + timeNeededForTravel
    return totalTime


def ternary_search_convex_function(low, high):
    thirdStepSize = (high - low) / 3
    firstPoint = low + thirdStepSize
    secondPoint = low + thirdStepSize*2
    firstResult = EuclideanTSP(firstPoint)
    secondResult = EuclideanTSP(secondPoint)
    if abs(firstResult - secondResult) < accuracy:
        return (firstResult, firstPoint)
    elif firstResult < secondResult:
        return ternary_search_convex_function(low, secondPoint)
    else:
        return ternary_search_convex_function(firstPoint, high)


inputs = list(map(float, sys.stdin.readline().split(' ')))
n = inputs[0]
p = inputs[1]
s = inputs[2]
v = inputs[3]

lowestBound = 0.1
highestBound = 100
accuracy = 0.000001

result = ternary_search_convex_function(lowestBound, highestBound)
print(str(result[0]) + " " + str(result[1]))