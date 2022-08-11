import sys

cardinalDirections = [(1,0), (0,1), (-1,0), (0,-1)]

def inGrid(positionToCheck):
    return positionToCheck[0] >= 0 and positionToCheck[0] < n \
        and positionToCheck[1] >= 0 and positionToCheck[1] < m

def bfs_iterative_grid(start, target):
    stack = [(start, 0)]
    discovered = set()

    while stack:
        stackItem = stack.pop(0)
        currentPosition = stackItem[0]
        steps = stackItem[1]
        if currentPosition == target:
            return steps
        discovered.add(currentPosition)
        value = grid[currentPosition[0]][currentPosition[1]]
        for direction in cardinalDirections:
            newPosition = (currentPosition[0] + value * direction[0], currentPosition[1] + value * direction[1])
            if inGrid(newPosition) and not newPosition in discovered:
                discovered.add(newPosition)
                stack.append((newPosition, steps+1))

    return -1
    
dimensions = list(map(int, sys.stdin.readline().split(' ')))
n = dimensions[0]
m = dimensions[1]

grid = [[] for _ in range(n)]

for rowNo in range(n):
    row = list(map(int, sys.stdin.readline().strip()))
    grid[rowNo] = row

result = bfs_iterative_grid((0,0), (n-1,m-1))
print(result)