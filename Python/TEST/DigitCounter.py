import math

d = 7
count = 0
for number in range(int(math.pow(10, d-1)), int(math.pow(10, d))):
    if not '9' in str(number):
        count += 1

print(count)