import sys


def distanceBetweenTwoNodes(node0, node1):
    return abs(node0[0] - node1[0]) + abs(node0[1] - node1[1])


def minKey(nofNodes, key, mstSet):
    min = sys.maxsize
    for v in range(nofNodes):
        if key[v] < min and mstSet[v] == False:
            min = key[v]
            min_index = v

    return (min, min_index)


def primMST(nofNodes):
    bestDistance = [sys.maxsize] * nofNodes
    mstSet = [False] * nofNodes

    bestDistance[0] = 0
    totalWeight = 0

    for _ in range(nofNodes):
        minTuple = minKey(nofNodes, bestDistance, mstSet)
        totalWeight += minTuple[0]
        currentNode = minTuple[1]
        mstSet[currentNode] = True
        for candidate in range(nofNodes):
            distance = distanceBetweenTwoNodes(
                nodeList[currentNode], nodeList[candidate])
            if mstSet[candidate] == False and bestDistance[candidate] > distance:
                bestDistance[candidate] = distance

    return totalWeight


##########################
sys.stdin = open('TEST/TestFile.txt', 'r')
##########################

nofNodes = int(sys.stdin.readline().strip())
nodeList = []

for node in range(nofNodes):
    node = tuple(map(int, sys.stdin.readline().strip().split(' ')))
    nodeList.append(node)


result = primMST(nofNodes)

print(result)
