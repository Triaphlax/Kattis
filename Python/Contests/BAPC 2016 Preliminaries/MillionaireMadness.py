import sys
import heapq

###################################
sys.stdin = open('TEST/TestFile.txt', 'r')
###################################


def dijkstra(source, target):
    bestLadder[source[1]][source[0]] = 0

    phq = [(0, source)]

    while len(phq) != 0:
        (ladderHeight, position) = heapq.heappop(phq)
        if position == target:
            return ladderHeight
        visited[position[1]][position[0]] = True

        for offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            neighborPosition = (
                position[0] + offset[0], position[1] + offset[1])
            neighborX, neighborY = neighborPosition
            if neighborX < 0 or neighborX >= width or neighborY < 0 or neighborY >= length:
                continue
            if not visited[neighborPosition[1]][neighborPosition[0]]:
                currentHeight = vault[position[1]][position[0]]
                neighborHeight = vault[neighborPosition[1]
                                       ][neighborPosition[0]]
                newLadderHeight = max(
                    ladderHeight, neighborHeight - currentHeight)
                oldLadderHeight = bestLadder[neighborPosition[1]
                                             ][neighborPosition[0]]
                if newLadderHeight < oldLadderHeight:
                    bestLadder[neighborPosition[1]
                               ][neighborPosition[0]] = newLadderHeight
                    heapq.heappush(phq, (newLadderHeight, neighborPosition))


length, width = list(map(int, sys.stdin.readline().strip().split(' ')))

vault = []
for _ in range(length):
    vault.append(list(map(int, sys.stdin.readline().strip().split(' '))))
visited = [[False for x in range(width)] for y in range(length)]
bestLadder = [[float("inf") for x in range(width)] for y in range(length)]

result = dijkstra((0, 0), (width-1, length-1))
print(result)
