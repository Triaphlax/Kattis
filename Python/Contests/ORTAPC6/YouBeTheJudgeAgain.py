import sys
import math


def getNewCoordinates(x, y, step):
    return (x+step[0], y+step[1])


def checkShape(x, y):
    shapeColor = grid[y][x]

    borderList = []
    stepList = [(0, -1), (1, -1), (1, 0), (1, 1),
                (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    for step in stepList:
        newX, newY = getNewCoordinates(x, y, step)
        if newX < 0 or newY < 0 or newX >= dimension or newY >= dimension:
            borderList.append(-1)
        else:
            borderList.append(grid[newY][newX])

    #borderList = borderList + [borderList[0], borderList[1]]
    shapeFound = False
    firstIndex = -1
    secondIndex = -1
    for start in range(8):
        if start == secondIndex:
            continue
        startBorderColor = borderList[start]
        if startBorderColor == shapeColor and shapeFound:
            return False, []
        elif startBorderColor == shapeColor:
            if borderList[(start + 1) % 8] == shapeColor:
                shapeFound = True
                firstIndex = start % 8
                secondIndex = (firstIndex+1) % 8
                continue
            elif borderList[(start + 2) % 8] == shapeColor:
                shapeFound = True
                firstIndex = start % 8
                secondIndex = (firstIndex+2) % 8
                continue
            elif borderList[(start - 2) % 8] == shapeColor:
                shapeFound = True
                firstIndex = start % 8
                secondIndex = (firstIndex-2) % 8
                continue
    if not shapeFound:
        return False, []
    else:
        return True, [(x, y), getNewCoordinates(x, y, stepList[firstIndex]), getNewCoordinates(x, y, stepList[secondIndex])]


################
sys.stdin = open('TEST/TestFile.txt', 'r')
################

exponent = int(sys.stdin.readline().strip())

dimension = int(math.pow(2, exponent))

nofColors = (int(math.pow(4, exponent)) - 1) // 3
colorDict = {color: (False, [])
             for color in range(nofColors + 1)}

grid = []
for rowNumber in range(dimension):
    row = list(map(int, sys.stdin.readline().strip().split(' ')))
    grid.append(row)

solved = False
broken = False
for y in range(dimension):
    row = grid[y]
    for x in range(dimension):
        element = row[x]
        if element == 0:
            if colorDict[element][0]:
                print(0)
                broken = True
                break
            else:
                colorDict[element] = (True, [(x, y)])
        else:
            colorFound, coordinates = colorDict[element]
            if colorFound:
                if (x, y) in coordinates:
                    continue
                else:
                    print(0)
                    broken = True
                    break
            else:
                isShape, coordinates = checkShape(x, y)
                if isShape:
                    colorDict[element] = (True, coordinates)
                else:
                    print(0)
                    broken = True
                    break
    if broken:
        break

if not broken:
    print(1)
