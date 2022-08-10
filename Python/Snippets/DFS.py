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

    return (path)

# def dfs_iterative(graph, start):
#     stack = [start]
#     discovered = set()

#     while stack:
#         node = stack.pop()
#         discovered.add(node)
#         for neighbor in graph[node]:
#             if not neighbor in discovered:
#                 discovered(neighbor)
#                 stack.append(neighbor)

#     return (discovered)