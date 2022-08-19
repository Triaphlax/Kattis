import sys


def gcd(a, b):

    while not a == 0:
        if a == 0:
            break
        else:
            temp = a
            a = b % a
            b = temp

    return b


numbers = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().strip().split(' ')))
answers = set()

previousDSet = set()
for i in range(numbers):
    newDSet = set()
    for element in previousDSet:
        answer = gcd(sequence[i], element)
        newDSet.add(answer)
        answers.add(answer)
    newDSet.add(sequence[i])
    answers.add(sequence[i])
    previousDSet = newDSet

print(len(answers))
