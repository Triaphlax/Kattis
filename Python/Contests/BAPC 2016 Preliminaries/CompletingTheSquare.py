import math
import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################

corners = []
for _ in range(3):
    baseCorner = tuple(map(int, sys.stdin.readline().strip().split(' ')))
    corners.append(baseCorner)

distances = []
for firstCornerIndex in range(3):
    firstCorner = corners[firstCornerIndex]
    secondCorner = corners[(firstCornerIndex + 1) % 3]
    distance = math.sqrt(
        sum(list(map(lambda a, b: pow(a - b, 2), firstCorner, secondCorner))))
    distances.append(distance)

inwardCorner = -1
outwardCorners = []
if distances[0] == distances[1]:
    inwardCorner = 1
    outwardCorners = [0, 2]
elif distances[1] == distances[2]:
    inwardCorner = 2
    outwardCorners = [0, 1]
elif distances[2] == distances[0]:
    inwardCorner = 0
    outwardCorners = [1, 2]

baseCorner = corners[outwardCorners[0]]
otherCorner = corners[outwardCorners[1]]
inwardCorner = corners[inwardCorner]
transposedCorner = tuple(map(lambda a, b: a - b, baseCorner, inwardCorner))
newCorner = tuple(map(lambda a, b: a + b, transposedCorner, otherCorner))


print(' '.join(list(map(str, newCorner))))
