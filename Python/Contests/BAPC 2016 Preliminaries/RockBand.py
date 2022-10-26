import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################

nofMembers, nofSongs = list(map(int, sys.stdin.readline().strip().split(' ')))
preferenceLists = []
for _ in range(nofMembers):
    preferenceLists.append(
        list(map(int, sys.stdin.readline().strip().split(' '))))

if nofMembers == 1:
    print(1)
    print(preferenceLists[0][0])
    exit()

occurancesList = {}
bestResult = nofSongs
for songIndex in range(nofSongs-1, -1, -1):
    for memberIndex in range(nofMembers):
        song = preferenceLists[memberIndex][songIndex]
        if not song in occurancesList:
            occurancesList[song] = nofMembers-1
        else:
            occurances = occurancesList[song]
            occurances -= 1
            if occurances == 0:
                del occurancesList[song]
            else:
                occurancesList[song] = occurances
    if len(occurancesList) == 0 and songIndex > 0:
        bestResult = songIndex

print(bestResult)
resultSlice = preferenceLists[0][0:bestResult]
resultSlice.sort()
print(" ".join(list(map(str, resultSlice))))
