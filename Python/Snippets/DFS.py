def dfs_iterative(graph, start):
    stack = [start]
    path = set()

    while stack:
        node = stack.pop()
        if node in path:
            continue
        path.add(node)
        for neighbor in graph[node]:
            stack.append(neighbor)

    return (path, sum)


allNodesToVisit = set(range(nofNodes))
graph = {new_list: [] for new_list in range(nofNodes)}

for road in range(nofRoads):
    road = list(map(int, sys.stdin.readline().strip().split(' ')))
    for endpointIndex in [0,1]:
        otherEndpointIndex = (endpointIndex + 1) % 2
        graph[road[endpointIndex]].append(road[otherEndpointIndex])