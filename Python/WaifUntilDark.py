import sys

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
            path_flow = min(path_flow, fullGraph[parent[nodeInPath]][nodeInPath])
            nodeInPath = parent[nodeInPath]

        max_flow += path_flow

        currentNode = target
        while(currentNode != source):
            previousNode = parent[currentNode]
            fullGraph[previousNode][currentNode] -= path_flow
            fullGraph[currentNode][previousNode] += path_flow
            currentNode = parent[currentNode]

    return max_flow

fullGraph = []

firstSettings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofChildren = firstSettings[0]
nofToys = firstSettings[1]
nofCategories = firstSettings[2]

nofNodes = 2 + nofChildren + nofToys + nofCategories
source = 0
target = nofNodes - 1

firstRow = [0]
firstRow.extend([1] * nofChildren)
firstRow.extend([0] * (nofNodes - (nofChildren + 1)))
fullGraph.append(firstRow)

firstOffset = nofChildren
for child in range(1, nofChildren+1):
    childSettings = list(map(int, sys.stdin.readline().strip().split(' ')))
    toysInterestedIn = childSettings[0]
    childRow = [0]*nofNodes
    for inputIndex in range(toysInterestedIn):
        toy = childSettings[1 + inputIndex]
        childRow[firstOffset + toy] = 1 # toy is 1-indexed
    fullGraph.append(childRow)

for toy in range(1, nofToys+1):
    toyRow = [0]*(nofNodes-1)
    toyRow.append(1)
    fullGraph.append(toyRow)

secondOffset = nofChildren + nofToys
for category in range(1, nofCategories+1):
    categorySettings = list(map(int, sys.stdin.readline().strip().split(' ')))
    nofToysInCategory = categorySettings[0]
    for inputIndex in range(nofToysInCategory):
        toyInCategory = categorySettings[1 + inputIndex]
        fullGraph[firstOffset + toyInCategory][nofNodes-1] = 0 # toy is 1-indexed
        fullGraph[firstOffset + toyInCategory][secondOffset + category] = 1 # category is 1-indexed
    categoryRow = [0]*(nofNodes-1)
    maximumToysFromCategory = categorySettings[-1]
    categoryRow.append(maximumToysFromCategory)
    fullGraph.append(categoryRow)

fullGraph.append([0]*nofNodes)

result = ford_fulkerson(source, target)
print(result)