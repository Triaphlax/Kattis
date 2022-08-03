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


allNodesToVisit = set(range(nofNodes))
graph = {new_list: [] for new_list in range(nofNodes)}

for road in range(nofRoads):
    road = list(map(int, sys.stdin.readline().strip().split(' ')))
    for endpointIndex in [0,1]:
        otherEndpointIndex = (endpointIndex + 1) % 2
        graph[road[endpointIndex]].append(road[otherEndpointIndex])