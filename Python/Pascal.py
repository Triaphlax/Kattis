import sys
import math

def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

n = int(sys.stdin.readline().strip(' '))

smallestDivisor = -1
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        smallestDivisor = i
        break

if smallestDivisor == -1:
    largestDivisor = 1
else:
    largestDivisor = int(n / smallestDivisor)
result = n - largestDivisor
print(result)

# counter = 0
# for i in range (n-1, 0, -1):
#     counter = counter + 1
#     if n % i == 0:
#         break
# print(counter)