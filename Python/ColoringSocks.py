import sys

firstSettings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofSocks = firstSettings[0]
maxCapacity = firstSettings[1]
maxDiff = firstSettings[2]

socks = list(map(int, sys.stdin.readline().strip().split(' ')))
socks.sort(reverse=True)

washTurns = 0
currentSockIndex = 0
while currentSockIndex < len(socks):
    largestSock = socks[currentSockIndex]
    currentSockIndex += 1
    capacity = 1
    while capacity < maxCapacity:
        if currentSockIndex < len(socks) and abs(socks[currentSockIndex] - largestSock) <= maxDiff:
            currentSockIndex += 1
            capacity += 1
        else:
            break
    washTurns += 1

print(washTurns)