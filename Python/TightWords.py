import sys

input = sys.stdin.readlines()

for line in input:
    settings = list(map(int, line.strip().split(' ')))
    alphabetSize = settings[0] + 1
    wordLength = settings[1]
    subsolutionTable = [ [float("-inf")]*alphabetSize for _ in [0,1]] 

    for currentPosition in range(wordLength):
        currentIndex = currentPosition % 2
        otherIndex = (currentIndex + 1) % 2 # subsolutions are number of tight words of length l ending in character c

        for i in range(alphabetSize):
            subsolution = -1
            if subsolutionTable[otherIndex][i] == float("-inf"):
                subsolution = 1
            else:
                upper = subsolutionTable[otherIndex][i+1] if i+1 <= alphabetSize-1 else 0
                middle = subsolutionTable[otherIndex][i]
                lower = subsolutionTable[otherIndex][i-1] if i-1 >= 0 else 0
                subsolution = upper + middle + lower
            subsolutionTable[currentIndex][i] = subsolution

    nofTightWords = sum(subsolutionTable[currentIndex])
    percentageOfTightWords = nofTightWords / pow(alphabetSize, wordLength)
    print("%.9f" % (percentageOfTightWords * 100))
