import sys


def bfs_iterative(graph, start):
    stack = [start]
    discovered = set()

    while stack:
        node = stack.pop(0)
        discovered.add(node)
        for neighbor in graph[node]:
            if not neighbor in discovered:
                discovered.add(neighbor)
                stack.append(neighbor)

    return (discovered)



firstInput = list(map(int, sys.stdin.readline().split(' ')))
nofNodes = firstInput[0]
nofEdges = firstInput[1]

allNodesToVisit = set(range(1, nofNodes+1))
graph = {node: [] for node in allNodesToVisit}

for edge in range(nofEdges):
    edgeData = list(map(int, sys.stdin.readline().split(' ')))
    for i in [0,1]:
        graph[edgeData[i]].append(edgeData[(i + 1) % 2])

connectedToInternet = bfs_iterative(graph, 1)
unconnectedToInternet = allNodesToVisit.difference(connectedToInternet)

if len(unconnectedToInternet) == 0:
    print("Connected")
else:
    for val in unconnectedToInternet:
        print(val)