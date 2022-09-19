import sys

################
sys.stdin = open('TEST/TestFile.txt', 'r')
################

firstPassword = sys.stdin.readline().strip()
secondPassword = sys.stdin.readline().strip()

nofSolutions = 1
for i in range(4):
    if firstPassword[i] != secondPassword[i]:
        nofSolutions *= 2

print(nofSolutions)
