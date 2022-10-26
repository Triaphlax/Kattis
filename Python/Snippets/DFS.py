def dfs_iterative(graph, start):
    dfsStack = [start]
    discovered = set()

    while dfsStack:
        node = dfsStack.pop()
        if node in discovered:
            continue
        discovered.add(node)
        for neighbor in graph[node]:
            dfsStack.append(neighbor)

    return discovered

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