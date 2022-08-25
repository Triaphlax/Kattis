import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################

input = sys.stdin.readlines()

for line in input:
    settings = list(map(int, line.strip().split(' ')))
# settings = list(map(int, sys.stdin.readline().strip().split(' ')))
print(str(settings[0] + settings[1]))
