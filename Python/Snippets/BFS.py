def bfs_iterative(graph, start):
    queue = [start]
    discovered = set()

    while queue:
        node = queue.pop()
        discovered.add(node)
        for neighbor in graph[node]:
            if not neighbor in discovered:
                discovered.add(neighbor)
                queue = [neighbor] + queue

    return (discovered)