import sys


######################
sys.stdin = open('TEST/TestFile.txt', 'r')
######################

nofMountains = int(sys.stdin.readline().strip())

mountainRange = []
for _ in range(nofMountains):
    height = int(sys.stdin.readline().strip())
    mountainRange.append(height)

largestAnswer = 1
for top in range(nofMountains):
    step = 1
    previousHeight = mountainRange[top]
    while True:
        endOne = top - step
        endTwo = top + step
        if endOne < 0 or endTwo < 0 or endOne >= nofMountains or endTwo >= nofMountains:
            break
        if not mountainRange[endOne] == mountainRange[endTwo]:
            break
        if mountainRange[endOne] >= previousHeight:
            break
        step += 1
        previousHeight = mountainRange[endOne]
    thisAnswer = 1 + 2*(step-1)
    if thisAnswer > largestAnswer:
        largestAnswer = thisAnswer

if largestAnswer == 1:
    print(-1)
else:
    print(largestAnswer)
