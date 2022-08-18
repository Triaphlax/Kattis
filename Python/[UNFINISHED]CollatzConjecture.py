import sys

def gcd(a, b):

    while not a == 0:
        if a == 0:
            break
        else:
            temp = a
            a = b%a
            b = temp
     
    return b

################################
sys.stdin = open('TEST/TestFile.txt', 'r')
################################'

numbers = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().strip().split(' ')))
answers = set(sequence)

print(gcd(80850,910))