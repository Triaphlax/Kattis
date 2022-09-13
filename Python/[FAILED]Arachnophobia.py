import sys
import queue
from wsgiref.handlers import format_date_time

class Graph:
    def __init__(self, nofNodes):
        self.nodeDict = {}
        self.minimumDistFromSpiderForTime = []
        self.closestSpiderDist = []
        self.nofNodes = nofNodes
        for nodeNumber in range(nofNodes):
            self.addNode(nodeNumber)

    def setSource(self, source):
        self.source = source

    def resetShortestPaths(self):
        self.nofNodes = len(self.nodeDict)
        for nodeNumber in range(nofNodes):
            self.nodeDict[nodeNumber].resetVisited()    
        self.minimumDistFromSpiderForTime = []
        for _ in range(nofNodes):
            self.minimumDistFromSpiderForTime.append({})
        if len(self.closestSpiderDist) == 0:
            self.closestSpiderDist = [float("inf")] * self.nofNodes

    def addNode(self, nodeNumber):
        self.node = Node(nodeNumber)
        self.nodeDict[nodeNumber] = self.node
    
    def addEdge(self, nodeFromNumber, nodeToNumber, edgeWeight):
        nodeFrom = self.nodeDict[nodeFromNumber]
        nodeFrom.addNeighbor(nodeToNumber, edgeWeight)
        nodeTo = self.nodeDict[nodeToNumber]
        nodeTo.addNeighbor(nodeFromNumber, edgeWeight)

    def getShortestPathFromSourceToNode(self, nodeNumber):
        if nodeNumber > self.nofNodes-1:
            return float("inf")
        return self.minimumDistFromSpiderForTime[nodeNumber]

    def dijkstraSpider(self):
        self.resetShortestPaths()

        self.closestSpiderDist[self.source] = 0

        pq = queue.PriorityQueue()
        pq.put((0, self.source))

        while not pq.empty():
            (currentDistance, currentNodeNumber) = pq.get()
            currentNode = self.nodeDict[currentNodeNumber]
            currentNode.setVisited()
            
            for neighborNodeNumber in currentNode.neighbors.keys():
                neighborNode = self.nodeDict[neighborNodeNumber]
                if not neighborNode.visited:
                    travelDistance = currentNode.getDistanceToNeighbor(neighborNodeNumber)
                    oldDistance = self.closestSpiderDist[neighborNodeNumber]
                    newDistance = currentDistance + travelDistance
                    if newDistance < oldDistance:
                        self.closestSpiderDist[neighborNodeNumber] = newDistance
                        pq.put((newDistance, neighborNodeNumber))

    def dijkstraAnthony(self, maxTime, destination):
        self.resetShortestPaths()

        pq = queue.PriorityQueue()
        pq.put((-1 * self.closestSpiderDist[self.source], maxTime, self.source))

        while not pq.empty():
            (minDistanceToSpider, timeLeft, currentNodeNumber) = pq.get()
            minDistanceToSpider = minDistanceToSpider * -1

            if currentNodeNumber == destination:
                return minDistanceToSpider

            currentNode = self.nodeDict[currentNodeNumber]
            currentNode.setBests(minDistanceToSpider, timeLeft)

            self.minimumDistFromSpiderForTime[currentNodeNumber][timeLeft] = True
            
            for neighborNodeNumber in currentNode.neighbors.keys():
                timeLeftIfMove = timeLeft - currentNode.getDistanceToNeighbor(neighborNodeNumber)
                if timeLeftIfMove >= 0 and not self.hasNodeBeenVisitedInAnthonyLoop(neighborNodeNumber, timeLeft):
                    distFromSpiderAtNeighbor = self.closestSpiderDist[neighborNodeNumber]
                    minDistFromSpiderOnPath = min(distFromSpiderAtNeighbor, minDistanceToSpider)
                    
                    neighborNode = self.nodeDict[neighborNodeNumber]
                    if minDistFromSpiderOnPath > neighborNode.bestSpiderDist or timeLeftIfMove > neighborNode.bestTimeRemaining:
                        self.minimumDistFromSpiderForTime[neighborNodeNumber][timeLeftIfMove] = False
                        neighborNode.setBests(minDistFromSpiderOnPath, timeLeftIfMove)
                        pq.put((minDistFromSpiderOnPath * -1, timeLeftIfMove, neighborNodeNumber))
        
        return -1

    def hasNodeBeenVisitedInAnthonyLoop(self, nodeNumber, timeLeft):
        return self.minimumDistFromSpiderForTime[nodeNumber][timeLeft] if timeLeft in self.minimumDistFromSpiderForTime[nodeNumber] else False


class Node:
    def __init__(self, nodeNumber):
        self.nodeNumber = nodeNumber
        self.neighbors = {}
        self.visited = False
        self.bestSpiderDist = float("-inf")
        self.bestTimeRemaining = float("-inf")

    def addNeighbor(self, neighborNumber, edgeWeight):
        self.neighbors[neighborNumber] = edgeWeight

    def setVisited(self):
        self.visited = True

    def resetVisited(self):
        self.visited = False

    def getDistanceToNeighbor(self, neighborNumber):
        return self.neighbors[neighborNumber]

    def setBests(self, spiderDist, timeRemaining):
        self.bestSpiderDist = max(self.bestSpiderDist, spiderDist)
        self.bestTimeRemaining = max(self.bestTimeRemaining, timeRemaining)

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################

nofNodes, nofEdges, maxTime = list(map(int, sys.stdin.readline().strip().split(' ')))

graph = Graph(nofNodes)

for _ in range(nofEdges):
    nodeFromNumber, nodeToNumber, edgeWeight = list(map(int, sys.stdin.readline().strip().split(' ')))
    graph.addEdge(nodeFromNumber, nodeToNumber, edgeWeight)

source, destination = list(map(int, sys.stdin.readline().strip().split(' ')))

spiderSettings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofSpiders = spiderSettings[0]
spiderList = spiderSettings[1:]

for spider in spiderList:
    graph.setSource(spider)
    graph.dijkstraSpider()

graph.setSource(source)
result = graph.dijkstraAnthony(maxTime, destination)

if result == -1:
    raise "Oops"
else:
    print(result)

