import sys

def find_cycles_iterative_dominos(graph, start):
    stack = [(start, False)]
    parentStack = []
    visitedInThisRun = set()

    while stack:
        currentNode, isTraceback = stack.pop()

        if not isTraceback:
            if currentNode in parentStack:
                indexInStack = parentStack.index(currentNode)
                nodesInCycle = parentStack[indexInStack:]
                return True, set(nodesInCycle), visitedInThisRun
            if currentNode in alreadyVisited or currentNode in visitedInThisRun:
                continue
            parentStack.append(currentNode)
            partStack = []
            partStack.append((currentNode, True))
            for neighbor in graph[currentNode]:
                partStack.append((neighbor, False))
            stack += partStack

        else:
            stackTopNode = parentStack.pop()
            visitedInThisRun.add(currentNode)
            if not stackTopNode == currentNode:
                raise "Big problem"

    return False, set(), visitedInThisRun

def find_leaves_iterative_dominos(graph, start):
    stack = [start]
    visitedInThisRun = set()
    leavesFoundInThisRun = set()

    while stack:
        currentNode = stack.pop()
        if currentNode in visitedInThisRun or currentNode in alreadyVisited:
            continue
        visitedInThisRun.add(currentNode)
        if len(graph[currentNode]) == 0:
            leavesFoundInThisRun.add(currentNode)
        for neighbor in graph[currentNode]:
            stack.append(neighbor)

    return leavesFoundInThisRun, visitedInThisRun

###########################
sys.stdin = open('TEST/TestFile.txt', 'r')
###########################

nofCases = int(sys.stdin.readline().strip())

for _ in range(nofCases):
    nofDominoes, nofConnections = list(map(int, sys.stdin.readline().strip().split(' ')))
    
    graph = {}
    for dominoNumber in range(1, nofDominoes + 1): # dominoes are 1-indexed
        graph[dominoNumber] = set()
    
    for _ in range(nofConnections):
        dominoIfFall, dominoThenFall = list(map(int, sys.stdin.readline().strip().split(' ')))
        graph[dominoThenFall].add(dominoIfFall)
    
    # remove cycles
    alreadyVisited = set()
    nodesLeftToVisit = set(range(1, nofDominoes + 1))
    while nodesLeftToVisit:
        startNode = nodesLeftToVisit.pop()
        nodesLeftToVisit.add(startNode)
        cycleFound, nodesInCycle, nodesVisitedInThisRun = find_cycles_iterative_dominos(graph, startNode)
        if cycleFound:
            homeNode = nodesInCycle.pop()
            nodesInCycle.add(homeNode)
            outgoingConnectionsOfCycle = set()
            for cycleNode in nodesInCycle:
                outgoingConnectionsOfCycle = outgoingConnectionsOfCycle.union(graph[cycleNode])
            for cycleNode in nodesInCycle:
                outgoingConnectionsOfCycle.discard(cycleNode)
            graph[homeNode] = outgoingConnectionsOfCycle
            for cycleNode in nodesInCycle:
                if not cycleNode == homeNode:
                    graph[cycleNode] = set([homeNode])
        alreadyVisited = alreadyVisited.union(nodesVisitedInThisRun)
        nodesLeftToVisit = nodesLeftToVisit.difference(nodesVisitedInThisRun)

    # get leaves
    alreadyVisited = set()
    nodesLeftToVisit = set(range(1, nofDominoes + 1))
    leafNodes = set()
    while nodesLeftToVisit:
        leafNodesFoundInThisRun, nodesVisitedInThisRun = find_leaves_iterative_dominos(graph, nodesLeftToVisit.pop())
        alreadyVisited = alreadyVisited.union(nodesVisitedInThisRun)
        leafNodes = leafNodes.union(leafNodesFoundInThisRun)
        nodesLeftToVisit = nodesLeftToVisit.difference(nodesVisitedInThisRun)

    print(len(leafNodes))