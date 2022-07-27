def dfs_iterative(graph, start):
    stack = [start]
    path = set()
    sum = 0

    while stack:
        node = stack.pop()
        if node in path:
            continue
        path.add(node)
        sum += graph[node][0]
        for neighbor in graph[node][1]:
            stack.append(neighbor)

    return (path, sum)


allNodesToVisit = set(range(nofNodes))
graph = {new_list: [] for new_list in range(nofNodes)}

for road in range(nofRoads):
    road = list(map(int, sys.stdin.readline().strip().split(' ')))
    for endpointIndex in [0,1]:
        otherEndpointIndex = (endpointIndex + 1) % 2
        graph[road[endpointIndex]].append(road[otherEndpointIndex])