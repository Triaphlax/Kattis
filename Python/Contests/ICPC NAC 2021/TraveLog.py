import sys
import heapq

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################

class Graph:
    def __init__(self, source, nodesList):
        self.nodeDict = {}
        self.source = source
        self.nofNodes = len(nodesList)
        for nodeKey in nodesList:
            self.addNode(nodeKey)
        self.edgeList = []

    def addNode(self, nodeKey):
        self.nodeDict[nodeKey] = Node(nodeKey)

    def nodeExists(self, nodeKey):
        return nodeKey in self.nodeDict

    def retrieveNode(self, nodeKey):
        if self.nodeExists(nodeKey):
            return self.nodeDict[nodeKey]
        else:
            raise "Node does not exist"

    def addEdge(self, nodeFrom, nodeTo, weight, isUndirected):
        nodeFromObject = self.nodeDict[nodeFrom]
        nodeFromObject.addNeighbor(nodeTo, weight)
        if isUndirected:
            nodeToObject = self.nodeDict[nodeTo]
            nodeToObject.addNeighbor(nodeFrom, weight)
        self.edgeList.append((nodeFrom, nodeTo, weight))


class Node:
    def __init__(self, nodeNumber):
        self.nodeNumber = nodeNumber
        self.neighbors = {}
        self.visited = False

    def addNeighbor(self, neighbor, edgeWeight):
        if neighbor in self.neighbors:
            self.neighbors[neighbor].append(edgeWeight)
        else:
            self.neighbors[neighbor] = [edgeWeight]

    def setVisited(self):
        self.visited = True

    def getDistancesToNeighbor(self, neighbor):
        return self.neighbors[neighbor]

    def getNeighbors(self):
        return list(self.neighbors.keys())


def dijkstra(graph, source):
    shortestDistances = {key: float("inf") for key in graph.nodeDict.keys()}
    shortestDistances[source] = 0

    phq = [(0, source)]
    heapq.heapify(phq)

    while len(phq) != 0:
        (distanceSoFar, node) = heapq.heappop(phq)
        nodeObject = graph.nodeDict[node]
        nodeObject.setVisited()

        for neighbor in nodeObject.neighbors.keys():
            neighborObject = graph.nodeDict[neighbor]
            if not neighborObject.visited:
                distances = nodeObject.getDistancesToNeighbor(neighbor)
                for travelDistance in distances:
                    oldDistance = shortestDistances[neighbor]
                    newDistance = distanceSoFar + travelDistance
                    if newDistance < oldDistance:
                        shortestDistances[neighbor] = newDistance
                        heapq.heappush(phq, (newDistance, neighbor))

    return shortestDistances

def binary_search_lower(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_lower(arr, low, mid - 1, x)
        else:
            return binary_search_lower(arr, mid + 1, high, x)
    else:
        return high

def binary_search_upper(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_upper(arr, low, mid - 1, x)
        else:
            return binary_search_upper(arr, mid + 1, high, x)
    else:
        return low

def toposort_iterative(graph, start):
    stack = [(start, False)]
    visitedInThisRun = set()

    while stack:
        currentNode, isTraceback = stack.pop()

        if not isTraceback:
            if currentNode in tsAlreadyVisited or currentNode in visitedInThisRun:
                continue
            visitedInThisRun.add(currentNode)
            partStack = []
            partStack.append((currentNode, True))
            currentNodeObject = graph.retrieveNode(currentNode)
            neighbors = currentNodeObject.getNeighbors()
            for neighbor in neighbors:
                partStack.append((neighbor, False))
            stack += partStack

        else:
            tsResultStack.append(currentNode)

    return visitedInThisRun


nofCities, nofRoads, nofData = list(
    map(int, sys.stdin.readline().strip().split(' ')))

nodeList = range(1, nofCities+1)
graph = Graph(1, nodeList)
for _ in range(nofRoads):
    fromNumber, toNumber, length = list(
        map(int, sys.stdin.readline().strip().split(' ')))
    graph.addEdge(fromNumber, toNumber, length, False)

corruptedLog = []
for _ in range(nofData):
    dataPoint = int(sys.stdin.readline().strip())
    corruptedLog.append(dataPoint)
corruptedLog.sort()

shortestDistances = dijkstra(graph, 1)
 
shortestDistance = shortestDistances[nofCities]
if corruptedLog[-1] > shortestDistance:
    print(0)
    exit()

validGraph = Graph(1, [])
for edge in graph.edgeList:
    nodeFrom, nodeTo, weight = edge
    distFrom = shortestDistances[nodeFrom]
    distTo = shortestDistances[nodeTo]
    if distFrom + weight == distTo:
        lowerBound = binary_search_lower(corruptedLog, 0, nofData - 1, distFrom)
        upperBound = binary_search_upper(corruptedLog, 0, nofData - 1, distTo)
        if upperBound - lowerBound <= 1:
            if not validGraph.nodeExists(nodeFrom):
                validGraph.addNode(nodeFrom)
            if not validGraph.nodeExists(nodeTo):
                validGraph.addNode(nodeTo)
            validGraph.addEdge(nodeFrom, nodeTo, weight, False)

tsLeftToVisit = set(validGraph.nodeDict.keys())
tsAlreadyVisited = set()
tsResultStack = []
while not len(tsLeftToVisit) == 0:
    tsVisitedThisIteration = toposort_iterative(validGraph, tsLeftToVisit.pop())
    tsLeftToVisit = tsLeftToVisit.difference(tsVisitedThisIteration)
    tsAlreadyVisited = tsAlreadyVisited.union(tsVisitedThisIteration)

ways = {nodeKey: (0, -1) for nodeKey in validGraph.nodeDict.keys()}
ways[1] = (1, -1)

for node in tsResultStack[::-1]:
    amount, predecessor = ways[node]
    nodeObject = validGraph.retrieveNode(node)
    neighbors = nodeObject.getNeighbors()
    for neighbor in neighbors:
        neighborAmount, neighborPredecessor = ways[neighbor]
        nofEdgesToNeighbor = len(nodeObject.getDistancesToNeighbor(neighbor))
        newAmount = neighborAmount + (amount * nofEdgesToNeighbor)
        newAmount = float("inf") if newAmount > 1 else newAmount
        newPredecessor = -1 if newAmount == 0 or newAmount == float("inf") else node
        ways[neighbor] = newAmount, newPredecessor

if not nofCities in ways:
    print(0)
else:
    resultAmount, resultPredecessor = ways[nofCities]
    if resultAmount == 0:
        print(0)
    elif resultAmount == float("inf"):
        print(1)
    else:
        bobsPath = [str(nofCities)]
        while resultPredecessor != -1:
            bobsPath = [str(resultPredecessor)] + bobsPath
            _, resultPredecessor = ways[resultPredecessor]
        print(len(bobsPath))
        print('\n'.join(bobsPath))