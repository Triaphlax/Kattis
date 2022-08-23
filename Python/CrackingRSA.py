import sys
import math

def phi(n):
    result = n
    for i in range (2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n = n // i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

nofCases = int(sys.stdin.readline().strip())

for _ in range(nofCases):
    nAndE = list(map(int, sys.stdin.readline().strip().split(' ')))
    n = nAndE[0]
    e = nAndE[1]
    totient = phi(n)

    for d in range(totient):
        if ((d - totient) * (e - totient)) % totient == 1:
            print(d)
            break