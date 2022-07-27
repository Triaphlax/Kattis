import sys


def dfs_friends_iterative(graph, start):
    stack = [start]
    path = set()
    sum = 0

    while stack:
        node = stack.pop()
        if node in path:
            continue
        path.add(node)
        sum += graph[node][0]
        for neighbor in graph[node][1]:
            stack.append(neighbor)

    return (path, sum)


firstInputs = list(map(int, sys.stdin.readline().strip().split(' ')))
nofFriends = firstInputs[0]
nofFriendships = firstInputs[1]

allNodesToVisit = set(range(nofFriends))
graph = {nodeInGraph: [0, []] for nodeInGraph in range(nofFriends)}

for friend in range(nofFriends):
    money = int(sys.stdin.readline())
    graph[friend][0] = money
    
for _ in range(nofFriendships):
    friendship = list(map(int, sys.stdin.readline().strip().split(' ')))
    for friendshipIndex in [0,1]:
        otherFriendshipIndex = (friendshipIndex + 1) % 2
        graph[friendship[friendshipIndex]][1].append(friendship[otherFriendshipIndex])

broken = False
while len(allNodesToVisit) > 0:
    dfsResult = dfs_friends_iterative(graph, allNodesToVisit.pop())
    allNodesToVisit = allNodesToVisit.difference(dfsResult[0])
    if dfsResult[1] != 0:
        print("IMPOSSIBLE")
        broken = True
        break

if not broken:
    print("POSSIBLE")