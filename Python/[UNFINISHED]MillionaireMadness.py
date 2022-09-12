import sys
import queue

class Graph:
    def __init__(self, source, nofNodes):
        self.nodeDict = {}
        self.source = source
        self.shortestDistFromSource = []
        self.nofNodes = nofNodes
        for nodeNumber in range(nofNodes):
            self.addNode(nodeNumber)
    
    def resetShortestPaths(self):
        self.nofNodes = len(self.nodeDict)
        self.shortestDistFromSource = [float("inf")] * self.nofNodes

    def addNode(self, nodeNumber):
        self.node = Node(nodeNumber)
        self.nodeDict[nodeNumber] = self.node

    def getNode(self, nodeNumber):
        if nodeNumber < 0 or nodeNumber >= self.nofNodes:
            raise "Node not in graph!"
        return self.nodeDict[nodeNumber]
    
    def addEdge(self, nodeFromNumber, nodeFromHeight, nodeToNumber, nodeToHeight):
        nodeFrom = self.nodeDict[nodeFromNumber]
        nodeFrom.addNeighbor(nodeToNumber, nodeToHeight)
        nodeTo = self.nodeDict[nodeToNumber]
        nodeTo.addNeighbor(nodeFromNumber, nodeFromHeight)

    def getShortestPathFromSourceToNode(self, nodeNumber):
        if nodeNumber > self.nofNodes-1:
            return float("inf")
        return self.shortestDistFromSource[nodeNumber]

    def dijkstra(self):
        self.resetShortestPaths()

        self.shortestDistFromSource[self.source] = 0

        pq = queue.PriorityQueue()
        pq.put((0, self.source))

        while not pq.empty():
            (ladderHeight, currentNodeNumber) = pq.get()
            currentNode = self.nodeDict[currentNodeNumber]
            currentNode.setVisited()
            
            for neighborNodeNumber in currentNode.neighbors.keys():
                neighborNode = self.nodeDict[neighborNodeNumber]
                if not neighborNode.visited:
                    extraLadderDistance = currentNode.getDistanceToNeighbor(neighborNodeNumber, ladderHeight)
                    oldLadderNecessary = self.shortestDistFromSource[neighborNodeNumber]
                    newLadderNecessary = ladderHeight + extraLadderDistance
                    if newLadderNecessary < oldLadderNecessary:
                        self.shortestDistFromSource[neighborNodeNumber] = newLadderNecessary
                        pq.put((newLadderNecessary, neighborNodeNumber))



class Node:
    def __init__(self, nodeNumber):
        self.nodeNumber = nodeNumber
        self.neighbors = {}
        self.visited = False
        self.height = -1

    def addNeighbor(self, neighborNumber, edgeWeight):
        self.neighbors[neighborNumber] = edgeWeight

    def setVisited(self):
        self.visited = True

    def getDistanceToNeighbor(self, neighborNumber, ladderHeight):
        neighborHeight = self.neighbors[neighborNumber]
        return max(0, neighborHeight - (self.height + ladderHeight))

    def initHeight(self, height):
        if self.height == -1:
            self.height = height

###################################
sys.stdin = open('TEST/TestFile.txt', 'r')
###################################

length, width = list(map(int, sys.stdin.readline().strip().split(' ')))

graph = Graph(0, length * width)

row1 = [-1] * width
row2 = [-1] * width

for rowNumber in range(length):
    row1 = row2 
    row2 = list(map(int, sys.stdin.readline().strip().split(' ')))

    for fullIndex in range(width * rowNumber, width * (rowNumber + 1)):
        currentNode = graph.getNode(fullIndex)
        currentHeight = row2[fullIndex % width]
        currentNode.initHeight(currentHeight)

        if not fullIndex < width:
            aboveIndex = fullIndex - width
            aboveHeight = row1[fullIndex % width]
            graph.addEdge(fullIndex, currentHeight, aboveIndex, aboveHeight)
        if not fullIndex % width == 0:
            leftIndex = fullIndex - 1
            leftHeight = row2[(fullIndex - 1) % width]
            graph.addEdge(fullIndex, currentHeight, leftIndex, leftHeight)

graph.dijkstra()

ladderHeight = graph.getShortestPathFromSourceToNode((width * length) - 1)
print(ladderHeight)