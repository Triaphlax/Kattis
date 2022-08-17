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
    
while True:
    input = sys.stdin.readline().strip()
    if input == "0 0":
        break
    pAndA = list(map(int, input.split(" ")))
    p = pAndA[0]
    a = pAndA[1]
    if isPrime(p):
        print("no")
        continue
    result = pow(a, p, p)
    if result == a:
        print("yes")
    else:
        print("no")