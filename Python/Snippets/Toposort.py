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

alreadyVisited = set()
resultStack = []