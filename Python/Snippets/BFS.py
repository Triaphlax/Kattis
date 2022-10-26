def bfs_iterative(graph, start):
    bfsQueue = [start]
    discovered = set()

    while bfsQueue:
        node = bfsQueue.pop()
        discovered.add(node)
        for neighbor in graph[node]:
            if not neighbor in discovered:
                discovered.add(neighbor)
                bfsQueue = [neighbor] + bfsQueue

    return (discovered)