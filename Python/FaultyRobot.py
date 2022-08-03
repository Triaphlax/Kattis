import sys


def bfs_iterative_faulty_robot(graph, startNode):
    stack = [(startNode, 1)]
    discovered = set()
    stopNodes = set()

    while stack:
        nodeInfo = stack.pop(0)
        currentNode = nodeInfo[0]
        buggedMovesLeft = nodeInfo[1]
        discovered.add(nodeInfo)

        # Forced Moves
        forcedNeighbor = graph[currentNode][0]
        if forcedNeighbor != None:
            if not (forcedNeighbor, buggedMovesLeft) in discovered:
                discovered.add((forcedNeighbor, buggedMovesLeft))
                stack.append((forcedNeighbor, buggedMovesLeft))

        # Bug Moves
        if buggedMovesLeft == 1:
            for bugNeighbor in graph[currentNode][1]:
                if not (bugNeighbor, 1) in discovered:
                    discovered.add((bugNeighbor, 0))
                    stack.append((bugNeighbor, 0))

        if forcedNeighbor == None:
            # Stay put
            if buggedMovesLeft == 1:
                if not (currentNode, 0) in discovered:
                    discovered.add((currentNode, 0))
                    stack.append((currentNode, 0))

            # Determine Stop Node
            if buggedMovesLeft == 0:
                stopNodes.add(currentNode)

    return (stopNodes)



firstInput = list(map(int, sys.stdin.readline().split(' ')))
nofNodes = firstInput[0]
nofEdges = firstInput[1]

allNodesInGraph = set(range(1, nofNodes+1))
graph = {node: [None, []] for node in allNodesInGraph}

for edge in range(nofEdges):
    edgeData = list(map(int, sys.stdin.readline().split(' ')))
    forcedMove = True if edgeData[0] < 0 else False
    if forcedMove:
        graph[abs(edgeData[0])][0] = edgeData[1]
    else:
        graph[edgeData[0]][1].append(edgeData[1])

stopNodes = bfs_iterative_faulty_robot(graph, 1)
print(len(stopNodes))