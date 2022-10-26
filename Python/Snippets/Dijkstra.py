import heapq

def dijkstra(graph, source):
    shortestDistances = {key: float("inf") for key in graph.nodeDict.keys()}
    shortestDistances[source] = 0

    phq = [(0, source)]
    heapq.heapify(phq)

    while len(phq) != 0:
        (distanceSoFar, node) = heapq.heappop(phq)
        nodeObject = graph.nodeDict[node]
        nodeObject.setVisited()

        for neighbor in nodeObject.neighbors.keys():
            neighborObject = graph.nodeDict[neighbor]
            if not neighborObject.visited:
                distances = nodeObject.getDistancesToNeighbor(neighbor)
                for travelDistance in distances:
                    oldDistance = shortestDistances[neighbor]
                    newDistance = distanceSoFar + travelDistance
                    if newDistance < oldDistance:
                        shortestDistances[neighbor] = newDistance
                        heapq.heappush(phq, (newDistance, neighbor))

    return shortestDistances