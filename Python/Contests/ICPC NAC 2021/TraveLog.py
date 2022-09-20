import sys
import queue

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################


class Graph:
    def __init__(self, source, nodesList):
        self.nodeDict = {}
        self.source = source
        self.shortestDistFromSource = {}
        self.nodesList = nodesList
        self.nofNodes = len(nodesList)
        for nodeNumber in nodesList:
            self.addNode(nodeNumber)

    def resetShortestPaths(self):
        self.nofNodes = len(self.nodeDict)
        self.shortestDistFromSource = {
            key: float("inf") for key in self.nodesList}

    def addNode(self, nodeNumber):
        self.node = Node(nodeNumber)
        self.nodeDict[nodeNumber] = self.node

    def addEdge(self, nodeFromNumber, nodeToNumber, edgeWeight):
        nodeFrom = self.nodeDict[nodeFromNumber]
        nodeFrom.addNeighbor(nodeToNumber, edgeWeight)

    def getShortestPathFromSourceToNode(self, nodeNumber):
        if nodeNumber > self.nofNodes-1:
            return float("inf")
        return self.shortestDistFromSource[nodeNumber]

    def dijkstra(self, fullDataLog):
        self.resetShortestPaths()

        self.shortestDistFromSource[self.source] = 0

        pq = queue.PriorityQueue()
        pq.put((0, self.source, [], 0))

        while not pq.empty():
            currentDistance, currentNodeNumber, currentRoute, currentDataIndex = pq.get()

            if currentNodeNumber == self.nofNodes:
                results.append(currentRoute + [currentNodeNumber])
                continue

            currentNode = self.nodeDict[currentNodeNumber]
            currentNode.setVisited()

            if currentDataIndex < len(fullDataLog):
                nextPoint = fullDataLog[currentDataIndex]
            else:
                nextPoint = float("inf")

            for neighborNodeNumber in currentNode.neighbors.keys():
                neighborNode = self.nodeDict[neighborNodeNumber]
                if not neighborNode.visited:
                    travelDistance = currentNode.getDistanceToNeighbor(
                        neighborNodeNumber)
                    oldDistance = self.shortestDistFromSource[neighborNodeNumber]
                    newDistance = currentDistance + travelDistance
                    if newDistance <= oldDistance and newDistance <= nextPoint:
                        self.shortestDistFromSource[neighborNodeNumber] = newDistance
                        if newDistance == nextPoint:
                            currentDataIndex += 1
                        pq.put((newDistance, neighborNodeNumber,
                               currentRoute + [currentNodeNumber], currentDataIndex))


class Node:
    def __init__(self, nodeNumber):
        self.nodeNumber = nodeNumber
        self.neighbors = {}
        self.visited = False

    def addNeighbor(self, neighborNumber, edgeWeight):
        self.neighbors[neighborNumber] = edgeWeight

    def setVisited(self):
        self.visited = True

    def getDistanceToNeighbor(self, neighborNumber):
        return self.neighbors[neighborNumber]


nofCities, nofRoads, nofData = list(
    map(int, sys.stdin.readline().strip().split(' ')))

graph = Graph(1, range(1, nofCities+1))

for _ in range(nofRoads):
    fromNumber, toNumber, length = list(
        map(int, sys.stdin.readline().strip().split(' ')))
    graph.addEdge(fromNumber, toNumber, length)

corruptedLog = []
for _ in range(nofData):
    dataPoint = int(sys.stdin.readline().strip())
    corruptedLog.append(dataPoint)
corruptedLog.sort()

results = []
graph.dijkstra(corruptedLog)

if len(results) == 0:
    print(0)
elif len(results) > 1:
    print(1)
else:
    print(len(results[0]))
    for i in range(len(results[0])):
        print(results[0][i])
