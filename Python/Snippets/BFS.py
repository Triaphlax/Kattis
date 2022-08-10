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