import sys
import math

numberOfHotSprings = int(sys.stdin.readline().strip())
hotSprings = list(map(int, sys.stdin.readline().strip().split(' ')))

hotSprings.sort()

midpoint = math.floor((len(hotSprings)-1)/2)

result = []
index = midpoint
step = 0
while abs(step) < numberOfHotSprings:
    index += step
    result.append(hotSprings[index])
    step = (abs(step) + 1) * int(math.pow(-1, step))

result = list(map(str, result))
print(" ".join(result))
