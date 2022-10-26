import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################


def perform_BFS(s, t, parent):
    queue = [s]
    discovered = set()

    while queue:
        currentNode = queue.pop()
        discovered.add(currentNode)
        for key, val in graph[currentNode].items():
            if key not in discovered and val > 0:
                discovered.add(key)
                queue.append(key)
                parent[key] = currentNode

    return t in discovered


def ford_fulkerson(source, target, nofNodes):
    parent = {key: -1 for key in graph.keys()}
    max_flow = 0

    while perform_BFS(source, target, parent):

        path_flow = float("Inf")
        nodeInPath = target
        while(nodeInPath != source):
            path_flow = min(
                path_flow, graph[parent[nodeInPath]][nodeInPath])
            nodeInPath = parent[nodeInPath]

        max_flow += path_flow

        currentNode = target
        while(currentNode != source):
            previousNode = parent[currentNode]
            graph[previousNode][currentNode] -= path_flow
            graph[currentNode][previousNode] += path_flow
            currentNode = parent[currentNode]

    return max_flow


nofRows, nofColumns = tuple(map(int, sys.stdin.readline().strip().split(' ')))

grid = []
for _ in range(nofRows):
    grid.append(list(sys.stdin.readline().strip()))

nonBorderEdges = set()
borderRegions = set()
#symbolPerRegion = {}
zeroRegionsNonBorder = set()
oneRegionsNonBorder = set()
coordinatesHandled = set()
regionPerCoordinate = {}
currentRegionNumber = 1
for i in range(nofRows):
    for j in range(nofColumns):
        if not (i, j) in coordinatesHandled:
            isBorderRegion = False
            queue = [(i, j)]

            while len(queue) != 0:
                current = queue.pop()
                currentSymbol = grid[current[0]][current[1]]
                coordinatesHandled.add(current)
                regionPerCoordinate[current] = currentRegionNumber
                for step in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    neighbor = (current[0] + step[0], current[1] + step[1])
                    if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= nofRows or neighbor[1] >= nofColumns:
                        isBorderRegion = True
                        continue
                    neighborSymbol = grid[neighbor[0]][neighbor[1]]
                    if neighbor in coordinatesHandled:
                        if neighborSymbol != currentSymbol:
                            neighborRegionNumber = regionPerCoordinate[neighbor]
                            nonBorderEdges.add(
                                (currentRegionNumber, neighborRegionNumber))
                            nonBorderEdges.add(
                                (neighborRegionNumber, currentRegionNumber))
                    else:
                        if neighborSymbol == currentSymbol:
                            queue.append((neighbor))

            if isBorderRegion:
                borderRegions.add(currentRegionNumber)
            else:
                if currentSymbol == '0':
                    zeroRegionsNonBorder.add(currentRegionNumber)
                elif currentSymbol == '1':
                    oneRegionsNonBorder.add(currentRegionNumber)
#            symbolPerRegion[currentRegionNumber] = currentSymbol
            currentRegionNumber += 1

nonBorderRegions = set(range(1, currentRegionNumber)
                       ).difference(set(borderRegions))

if len(nonBorderRegions) == 0 or len(nonBorderEdges) == 1:
    print(len(borderRegions))
    exit()

#  make bipartite graph
graph = {}
graph['source'] = {}
graph['target'] = {}
for region in nonBorderRegions:
    graph[region] = {}

for edge in nonBorderEdges:
    fromRegion, toRegion = edge
    if fromRegion in borderRegions or toRegion in borderRegions:
        continue
    graph[fromRegion][toRegion] = 1

for zeroRegion in zeroRegionsNonBorder:
    graph['source'][zeroRegion] = 1
    graph[zeroRegion]['source'] = 1

for oneRegion in oneRegionsNonBorder:
    graph['target'][oneRegion] = 1
    graph[oneRegion]['target'] = 1

x = ford_fulkerson('source', 'target', len(graph))
print(x + len(borderRegions))
