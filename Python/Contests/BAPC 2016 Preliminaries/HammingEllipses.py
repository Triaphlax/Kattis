import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################


def get_subsolution(length, distance):
    key = (length, distance)
    if key in subsolutions:
        return subsolutions[key]
    if length <= 0:
        return 0
    if distance < 0:
        return 0
    isDuplicate = duplicates[length-1]
    if isDuplicate:
        subsolution = get_subsolution(
            length-1, distance) + get_subsolution(length-1, distance-2)*(alphabetSize-1)
    else:
        subsolution = get_subsolution(
            length-1, distance-1)*(2) + get_subsolution(length-1, distance-2)*(alphabetSize-2)
    subsolutions[key] = subsolution
    return subsolution


alphabetSize, wordLength, requiredDistance = list(
    map(int, sys.stdin.readline().strip().split(' ')))
firstPoint = list(sys.stdin.readline().strip())
secondPoint = list(sys.stdin.readline().strip())

duplicates = [False] * wordLength
for i in range(wordLength):
    if firstPoint[i] == secondPoint[i]:
        duplicates[i] = True

subsolutions = {(0, 0): 1}
print(get_subsolution(wordLength, requiredDistance))
