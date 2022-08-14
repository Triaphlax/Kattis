import sys
import math


settings = list(map(int, sys.stdin.readline().strip().split(' ')))
maxOperations = settings[0]
maxInput = settings[1] 
algorithmComplexity = settings[2]

operationsNeeded = 0
if algorithmComplexity == 1:
    if maxInput > 13:
        operationsNeeded = 1000000001
    else:
        operationsNeeded = math.factorial(maxInput)
elif algorithmComplexity == 2:
        operationsNeeded = pow(2, maxInput)
elif algorithmComplexity == 3:
        operationsNeeded = pow(maxInput, 4)
elif algorithmComplexity == 4:
        operationsNeeded = pow(maxInput, 3)
elif algorithmComplexity == 5:
        operationsNeeded = pow(maxInput, 2)
elif algorithmComplexity == 6:
        operationsNeeded = maxInput * math.log2(maxInput)
elif algorithmComplexity == 7: 
        operationsNeeded = maxInput

if operationsNeeded <= maxOperations:
    print("AC")
else:
    print("TLE")