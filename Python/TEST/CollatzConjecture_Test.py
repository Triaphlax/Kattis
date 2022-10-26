import random

f = open("TEST/CollatzConjecture_Test.txt", 'a')
f.truncate(0)

amount = 500000
f.write(str(amount) + '\n')
sequence = ""
for i in range(amount):
    x = random.randint(0, 1000000000000000000)
    sequence += "" + str(x) + " "

f.write(sequence)
f.close()
