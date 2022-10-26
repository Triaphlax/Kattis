import random

f = open("TEST/Brexit_Test.txt", 'a')
f.truncate(0)

nofCountries = 200000
nofPartnerships = 199999
homeCountry = random.randint(0, nofCountries)
firstToLeave = random.randint(0, nofCountries)
f.write(str(nofCountries) + ' ' + str(nofPartnerships) + ' ' + str(homeCountry) + ' ' + str(firstToLeave) + '\n')
for i in range(1, nofPartnerships+1):
    x = i
    y = i + 1

    # x = (i // nofCountries) + 1
    # y = (i % nofCountries) + 1

    # while x == y:
    #     x = random.randint(1, nofCountries)
    #     y = random.randint(1, nofCountries)
    f.write(str(x) + ' ' + str(y) + '\n')

f.close()
