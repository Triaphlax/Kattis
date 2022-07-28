import sys
import math

firstInputs = sys.stdin.readline().split(' ')
nofPieSlices = int(firstInputs[0])
nofHalfRings = int(firstInputs[1])
radius = float(firstInputs[2])

secondInputs = sys.stdin.readline().split(' ')
ax = int(secondInputs[0])
ay = int(secondInputs[1])
bx = int(secondInputs[2])
by = int(secondInputs[3])

result = sys.maxsize

for chosenHalfRing in range(0, nofHalfRings):
    distanceTravelled = 0

    # Traverse half ring
    pieSlicesTravelled = abs(ax - bx)
    circumferenceHalfCircle = math.pi * \
        (radius * (chosenHalfRing / nofHalfRings))
    distanceTravelled += circumferenceHalfCircle * \
        (pieSlicesTravelled / nofPieSlices)

    # Get to chosen half ring
    halfRingsTravelled = abs(ay - chosenHalfRing) + abs(by - chosenHalfRing)
    distanceTravelled += radius * (halfRingsTravelled / nofHalfRings)

    if distanceTravelled < result:
        result = distanceTravelled

print(result)
