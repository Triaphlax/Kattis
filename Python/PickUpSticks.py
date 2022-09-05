import sys

def no_cycles_iterative(graph, start):
    stack = [(start, False)]
    parentStack = []
    visitedInThisRun = set()

    while stack:
        currentNode, isTraceback = stack.pop()

        if not isTraceback:
            if currentNode in parentStack:
                return False, set()
            if currentNode in alreadyVisited or currentNode in visitedInThisRun:
                continue
            visitedInThisRun.add(currentNode)
            parentStack.append(currentNode)
            partStack = []
            partStack.append((currentNode, True))
            for neighbor in graph[currentNode]:
                partStack.append((neighbor, False))
            stack += partStack

        else:
            stackTopNode = parentStack.pop()
            if not stackTopNode == currentNode:
                raise "Big problem"

    return True, visitedInThisRun

def toposort_iterative(graph, start):
    stack = [(start, False)]
    visitedInThisRun = set()

    while stack:
        currentNode, isTraceback = stack.pop()

        if not isTraceback:
            if currentNode in alreadyVisited or currentNode in visitedInThisRun:
                continue
            visitedInThisRun.add(currentNode)
            partStack = []
            partStack.append((currentNode, True))
            for neighbor in graph[currentNode]:
                partStack.append((neighbor, False))
            stack += partStack

        else:
            resultStack.append(currentNode)

    return visitedInThisRun

settings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofSticks = settings[0]
nofConnections = settings[1]

graph = {}
for stick in range(1, nofSticks+1): # sticks are 1-indexed
    graph[stick] = []

for connection in range(nofConnections):
    connectionSettings = list(map(int, sys.stdin.readline().strip().split(' ')))
    graph[connectionSettings[0]].append(connectionSettings[1])

nodesLeftToVisit = set(range(1, nofSticks+1))
alreadyVisited = set()
while nodesLeftToVisit:
    hasNoCycles, visitedInThisRun = no_cycles_iterative(graph, nodesLeftToVisit.pop())
    if not hasNoCycles:
        break
    nodesLeftToVisit = nodesLeftToVisit.difference(visitedInThisRun)
    alreadyVisited = alreadyVisited.union(visitedInThisRun)

if not hasNoCycles:
    print("IMPOSSIBLE")
else:
    nodesLeftToVisit = set(range(1, nofSticks+1))
    alreadyVisited = set()
    resultStack = []
    while nodesLeftToVisit:
        visitedInThisRun = toposort_iterative(graph, nodesLeftToVisit.pop())
        if not hasNoCycles:
            break
        nodesLeftToVisit = nodesLeftToVisit.difference(visitedInThisRun)
        alreadyVisited = alreadyVisited.union(visitedInThisRun)

    for index in range(nofSticks - 1, -1, -1):
        print(str(resultStack[index]))