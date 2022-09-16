import sys


def isBorder(x, y):
    return x == 0 or y == 0 or x == width - 1 or y == length - 1


def bfs_iterative_escape_wall_maria(start):
    queue = [(start, 0)]
    discovered = set()

    if isBorder(start[0], start[1]):
        return 0

    while queue:
        (node, steps) = queue.pop()
        discovered.add(node)

        if steps > timeLimit:
            break

        for step in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighborCoordinates = (node[0] + step[0], node[1] + step[1])
            square = wallMaria[neighborCoordinates[1]][neighborCoordinates[0]]

            if square == '1' or square == 'S':
                continue
            else:
                if square == 'U' and not step == (0, 1):
                    continue
                if square == 'D' and not step == (0, -1):
                    continue
                if square == 'R' and not step == (-1, 0):
                    continue
                if square == 'L' and not step == (1, 0):
                    continue
                if not neighborCoordinates in discovered:
                    if isBorder(neighborCoordinates[0], neighborCoordinates[1]) and steps < timeLimit:
                        return steps+1
                    discovered.add(neighborCoordinates)
                    queue = [(neighborCoordinates, steps+1)] + queue

    return -1


######################
sys.stdin = open('/TEST/TestFile.txt', 'r')
######################

timeLimit, length, width = list(
    map(int, sys.stdin.readline().strip().split(' ')))

wallMaria = []
sLocation = (-1, -1)

for rowNumber in range(length):
    row = sys.stdin.readline().strip()
    if 'S' in row:
        x = row.index('S')
        y = rowNumber
        sLocation = (x, y)
    wallMaria.append(row)

result = bfs_iterative_escape_wall_maria(sLocation)
if result == -1:
    print("NOT POSSIBLE")
else:
    print(str(result))
