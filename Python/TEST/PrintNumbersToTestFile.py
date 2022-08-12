import random

f = open("Python/Python/TEST/TestFile.txt", 'a')

amount = 10000
f.write(str(amount) + '\n')
for i in range(amount):
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    result = "" + str(x) + " " + str(y) + '\n'
    f.write(result)

# string = " "

# for i in range(100000):
#     string = string + str(i)
#     string = string + " "

# f.write(string)


f.close()
