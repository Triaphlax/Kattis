import sys


def minKey(nofNodes, key, mstSet):
    min = sys.maxsize
    for v in range(nofNodes):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return (min, min_index)


def primMST(graph):
    nofNodes = len(graph)
    bestDistance = [sys.maxsize] * nofNodes
    parent = [None] * nofNodes
    mstSet = [False] * nofNodes

    bestDistance[0] = 0
    parent[0] = -1
    totalWeight = 0

    for _ in range(nofNodes):
        minTuple = minKey(nofNodes, bestDistance, mstSet)
        totalWeight += minTuple[0]
        currentNode = minTuple[1]
        mstSet[currentNode] = True
        for candidate in range(nofNodes):
            if graph[currentNode][candidate] >= 0 and mstSet[candidate] == False and bestDistance[candidate] > graph[currentNode][candidate]:
                bestDistance[candidate] = graph[currentNode][candidate]
                parent[candidate] = currentNode

    return totalWeight


graph = [[0, 2, -1, 6, -1],
         [2, 0, 3, 8, 5],
         [-1, 3, 0, -1, 7],
         [6, 8, -1, 0, 9],
         [-1, 5, 7, 9, 0]]

result = primMST(graph)

print(result)
