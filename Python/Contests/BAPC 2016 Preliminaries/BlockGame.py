import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################


def get_subsolution(state):
    if state in subsolutions:
        return subsolutions[state]
    first, second = state
    if first == 0 or second == 0:
        subsolutions[state] = False
        return False
    if first == 1 or second == 1:
        subsolutions[state] = True
        return True
    if first == second:
        subsolutions[state] = True
        return True
    for move in range(first - (first % second), 0, -second):
        newTower = first - move
        if newTower >= second:
            newState = (newTower, second)
        else:
            newState = (second, newTower)
        subsolution = get_subsolution(newState)
        if not subsolution:
            subsolutions[state] = True
            return True
    subsolutions[state] = False
    return False


#############################
# import random
# for case in range(1123456):

#     first = random.randint(1, 1000000000000000000)
#     second = random.randint(1, first)
############################

first, second = list(map(int, sys.stdin.readline().strip().split(' ')))
subsolutions = {}

if first >= second:
    state = (first, second)
else:
    state = (second, first)
result = get_subsolution(state)
if result:
    print('win')
else:
    print('lose')
