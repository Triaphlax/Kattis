import random

f = open("TEST/ThePaladin_Test.txt", 'a')
f.truncate(0)

letters = "abcdefghijklmnopqrstuvwxyz"
nofPairs = 676
chainLength = 100
f.write(str(nofPairs) + ' ' + str(chainLength) + '\n')
for i in range(0, nofPairs):
    first = i // 26
    second = i % 26
    f.write(str(letters[first]) + str(letters[second]) + ' ' + str(random.randint(1, 100)) + '\n')

f.close()
