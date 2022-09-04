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


alreadyVisited = set()