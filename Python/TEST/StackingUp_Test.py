import random

f = open("TEST/StackingUp_Test.txt", 'a')

amount = 1000
f.write(str(amount) + '\n')
result = ""
x = 100000
for i in range(amount):
    x -= 1
    result += str(x) + ' '

f.write(result)
f.close()
