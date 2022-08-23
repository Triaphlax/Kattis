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