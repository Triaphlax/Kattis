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
    
    def addEdge(self, nodeFromNumber, nodeToNumber, edgeWeight):
        nodeFrom = self.nodeDict[nodeFromNumber]
        nodeFrom.addNeighbor(nodeToNumber, edgeWeight)

    def getShortestPathFromSourceToNode(self, nodeNumber):
        if nodeNumber > nofNodes-1:
            return float("inf")
        return self.shortestDistFromSource[nodeNumber]

    def dijkstra(self):
        self.resetShortestPaths()

        self.shortestDistFromSource[self.source] = 0

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
                    oldDistance = self.shortestDistFromSource[neighborNodeNumber]
                    newDistance = currentDistance + travelDistance
                    if newDistance < oldDistance:
                        self.shortestDistFromSource[neighborNodeNumber] = newDistance
                        pq.put((newDistance, neighborNodeNumber))



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

  

while True:
    settingsLine = sys.stdin.readline().strip()
    if settingsLine == '0 0 0 0':
        break
    nofNodes, nofEdges, nofQueries, sourceNodeNumber = list(map(int, settingsLine.split(' ')))

    graph = Graph(sourceNodeNumber, nofNodes)

    for _ in range(nofEdges):
        node1Number, node2Number, edgeWeight = list(map(int, sys.stdin.readline().strip().split(' ')))
        graph.addEdge(node1Number, node2Number, edgeWeight)

    graph.dijkstra()

    for _ in range(nofQueries):
        queryNode = int(sys.stdin.readline().strip())
        result = graph.getShortestPathFromSourceToNode(queryNode)
        if result < float("inf"):
            print(result)
        else:
            print("Impossible")

    print("")