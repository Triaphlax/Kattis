import sys 

def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


nofCases = int(sys.stdin.readline())

for case in range(nofCases):
    nofNodes = int(sys.stdin.readline())
    nofRoads = int(sys.stdin.readline())

    allNodesToVisit = set(range(nofNodes))
    graph = {new_list: [] for new_list in range(nofNodes)}
    
    for road in range(nofRoads):
        road = list(map(int, sys.stdin.readline().strip().split(' ')))
        for endpointIndex in [0,1]:
            otherEndpointIndex = (endpointIndex + 1) % 2
            graph[road[endpointIndex]].append(road[otherEndpointIndex])

    connectedComponents = 0
    while len(allNodesToVisit) != 0:
        connectedComponents += 1
        visitedInThisComponent = set()
        dfs(visitedInThisComponent, graph, allNodesToVisit.pop())
        allNodesToVisit = allNodesToVisit.difference(visitedInThisComponent)

    print(connectedComponents - 1)