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

tsLeftToVisit = set() # Fill in starting node list here
tsAlreadyVisited = set()
tsResultStack = []
while not len(tsLeftToVisit) == 0:
    tsVisitedThisIteration = toposort_iterative(validGraph, tsLeftToVisit.pop())
    tsLeftToVisit = tsLeftToVisit.difference(tsVisitedThisIteration)
    tsAlreadyVisited = tsAlreadyVisited.union(tsVisitedThisIteration)