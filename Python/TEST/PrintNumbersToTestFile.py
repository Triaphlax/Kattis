f = open("TEST/TestFile.txt", 'a')
string = " "

for i in range(100000):
    string = string + str(i)
    string = string + " "

f.write(string)
f.close()