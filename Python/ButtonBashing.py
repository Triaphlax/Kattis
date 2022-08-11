from dis import dis
import sys

def getDistance(current, target):
    return abs(current - target) if current >= target else sys.maxsize

def bfs_iterative_button_bashing(start):
    stack = [(start, 0)]
    discovered = set()

    bestResult = (0, getDistance(start, target))

    while stack:
        stackItem = stack.pop(0)
        currentTime = stackItem[0]
        buttonsPressed = stackItem[1]
        discovered.add(currentTime)
        distanceFromTarget = getDistance(currentTime, target)
        if bestResult[1] > distanceFromTarget:
            bestResult = (buttonsPressed, distanceFromTarget)
        if currentTime == target:
            break
        for nextButtonToPress in buttons:
            nextTime = currentTime + nextButtonToPress
            nextTime = 0 if nextTime < 0 else nextTime
            nextTime = 3600 if nextTime > 3600 else nextTime
            if not nextTime in discovered:
                discovered.add(nextTime)
                stack.append((nextTime, buttonsPressed + 1))

    return bestResult

nofCases = int(sys.stdin.readline())

for case in range(nofCases):
    settings = list(map(int, sys.stdin.readline().split(' ')))
    nofButtons = settings[0]
    target = settings[1]

    buttons = list(map(int, sys.stdin.readline().split(' ')))

    result = bfs_iterative_button_bashing(0)
    
    print(str(result[0]) + ' ' + str(result[1]))