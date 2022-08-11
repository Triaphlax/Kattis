def bfs_iterative(graph, start):
    queue = [start]
    discovered = set()

    while queue:
        node = queue.pop(0)
        discovered.add(node)
        for neighbor in graph[node]:
            if not neighbor in discovered:
                discovered.add(neighbor)
                queue.append(neighbor)

    return (discovered)