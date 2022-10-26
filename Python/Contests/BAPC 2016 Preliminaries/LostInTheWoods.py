import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################


def matrix_multiplication(A, B):
    zip_b = list(zip(*B))
    C = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
          for col_b in zip_b] for row_a in A]
    return C


def markov_transition(vector, markovMatrix, error):
    expectedValue = 0
    currentVector = vector
    remainingProbability = sum(vector[0])
    steps = 0
    while remainingProbability >= error:
        steps += 1
        currentVector = matrix_multiplication(currentVector, markovMatrix)
        expectedValue += steps * currentVector[0][nofNodes-1]
        remainingProbability -= currentVector[0][nofNodes-1]
        currentVector[0][nofNodes-1] = 0
    return expectedValue


nofNodes, nofEdges = list(map(int, sys.stdin.readline().strip().split(' ')))
graph = {node: {} for node in range(nofNodes)}
for _ in range(nofEdges):
    edgeFrom, edgeTo = list(map(int, sys.stdin.readline().strip().split(' ')))
    graph[edgeFrom][edgeTo] = 1
    graph[edgeTo][edgeFrom] = 1

markovMatrix = [[0 for _ in range(nofNodes)] for _ in range(nofNodes)]
for node in graph.keys():
    probability = float(1/len(graph[node].keys()))
    for neighbor in graph[node].keys():
        markovMatrix[node][neighbor] = probability

startingVector = [[1] + [0] * (nofNodes-1)]

solution = markov_transition(startingVector, markovMatrix, 0.000000001)
print("{:.5f}".format(solution))
