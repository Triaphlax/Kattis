import random

f = open("TEST/GameNight_Test.txt", 'a')
f.truncate(0)

amount = 9999
f.write(str(amount) + '\n')
seating = ""
for i in range(amount // 3):
    seating += "ABC"

f.write(seating)
f.close()
