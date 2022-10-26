def perform_BFS(s, t, parent):
    queue = [s]
    discovered = set()

    while queue:
        currentNode = queue.pop(0)
        discovered.add(currentNode)
        for ind, val in enumerate(fullGraph[currentNode]):
            if ind not in discovered and val > 0:
                discovered.add(ind)
                queue.append(ind)
                parent[ind] = currentNode

    return t in discovered


def ford_fulkerson(source, target):
    parent = [-1] * nofNodes
    max_flow = 0

    while perform_BFS(source, target, parent):

        path_flow = float("Inf")
        nodeInPath = target
        while(nodeInPath != source):
            path_flow = min(
                path_flow, fullGraph[parent[nodeInPath]][nodeInPath])
            nodeInPath = parent[nodeInPath]

        max_flow += path_flow

        currentNode = target
        while(currentNode != source):
            previousNode = parent[currentNode]
            fullGraph[previousNode][currentNode] -= path_flow
            fullGraph[currentNode][previousNode] += path_flow
            currentNode = parent[currentNode]

    return max_flow


fullGraph = [[0, 8, 0, 0, 3, 0],
             [0, 0, 9, 0, 0, 0],
             [0, 0, 0, 0, 7, 2],
             [0, 0, 0, 0, 0, 5],
             [0, 0, 7, 4, 0, 0],
             [0, 0, 0, 0, 0, 0]]
nofNodes = len(fullGraph)

source = 0
target = 5

result = ford_fulkerson(source, target)
print(result)
