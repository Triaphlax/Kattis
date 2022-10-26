import random

f = open("TEST/TestFile.txt", 'a')
f.truncate(0)

amount = 10000
f.write(str(amount) + '\n')
for i in range(amount):
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    result = "" + str(x) + " " + str(y) + '\n'
    f.write(result)

f.close()
