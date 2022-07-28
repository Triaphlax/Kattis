def dfs_iterative_weak_vertices(graph, start):
    stack = [(start, -1, -1)]
    visited = set()
    triangleNodes = set()

    while stack:
        tuple = stack.pop()
        node = tuple[0]
        oneAgo = tuple[1]
        twoAgo = tuple[2]
        if twoAgo >= 0 and twoAgo in graph[node]:
            triangleNodes.update([node, oneAgo, twoAgo])
        if node in visited:
            continue
        visited.add(node)
        for neighbor in graph[node]:
            stack.append((neighbor, node, oneAgo))

    return (visited, triangleNodes)


import sys

while True:
    nofNodes = int(sys.stdin.readline())
    if nofNodes == -1:
        break
    
    nodesLeftToVisit = set(range(nofNodes))
    graph = {new_list: [] for new_list in range(nofNodes)}

    for i in range(nofNodes):
        adjacencyLine = list(map(int, sys.stdin.readline().split(' ')))
        for j in range(len(adjacencyLine)):
            if adjacencyLine[j] == 1:
                graph[i].append(j)

    nodesLeftToVisit = set(range(nofNodes))
    potentialWeakNodes = set(range(nofNodes))
    while not len(nodesLeftToVisit) == 0:
        nodesVisited, triangleNodes = dfs_iterative_weak_vertices(graph, nodesLeftToVisit.pop())
        nodesLeftToVisit = nodesLeftToVisit.difference(nodesVisited)
        potentialWeakNodes = potentialWeakNodes.difference(triangleNodes)

    resultList = list(potentialWeakNodes)
    resultList.sort()
    print(" ".join(list(map(str, resultList))))
