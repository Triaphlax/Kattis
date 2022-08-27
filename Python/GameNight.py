import sys 

def compareDifferencesStrings(s, t):
    differences = 0
    if len(s) != len(t):
        return float("-inf")
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                differences += 1
        return differences

people = int(sys.stdin.readline().strip())
seating = sys.stdin.readline().strip()

nofAs = seating.count('A')
nofBs = seating.count('B')
nofCs = seating.count('C')

ABCstring = "A"*nofAs + "B"*nofBs + "C"*nofCs
finalAinABC = nofAs - 1
finalBinABC = nofAs + nofBs - 1
finalCinABC = people - 1
ACBstring = "A"*nofAs + "C"*nofCs + "B"*nofBs
finalAinACB = nofAs - 1
finalCinACB = nofAs + nofCs - 1
finalBinACB = people - 1
bestResult = float("inf")

ABCDict = {
    'AA': -1,
    'AB': +1,
    'AC': 0,
    'BA': 0,
    'BB': -1,
    'BC': +1,
    'CA': +1,
    'CB': 0,
    'CC': -1}
ACBDict = {
    'AA': -1,
    'AB': 0,
    'AC': +1,
    'BA': +1,
    'BB': -1,
    'BC': 0,
    'CA': 0,
    'CB': +1,
    'CC': -1}

#ABC
for startingIndex in range(len(seating)):
    if startingIndex == 0:
        diffScore = compareDifferencesStrings(seating, ABCstring)
    else:
        diffPartA = ABCDict['A' + seating[(finalAinABC + startingIndex) % people]] 
        diffPartB = ABCDict['B' + seating[(finalBinABC + startingIndex) % people]] 
        diffPartC = ABCDict['C' + seating[(finalCinABC + startingIndex) % people]]
        diffScore = diffScore + diffPartA + diffPartB + diffPartC
    if bestResult > diffScore:
        bestResult = diffScore

#ACB
for startingIndex in range(len(seating)):
    if startingIndex == 0:
        diffScore = compareDifferencesStrings(seating, ACBstring)
    else:
        diffPartA = ACBDict['A' + seating[(finalAinACB + startingIndex) % people]] 
        diffPartB = ACBDict['B' + seating[(finalBinACB + startingIndex) % people]] 
        diffPartC = ACBDict['C' + seating[(finalCinACB + startingIndex) % people]]
        diffScore = diffScore + diffPartA + diffPartB + diffPartC
    if bestResult > diffScore:
        bestResult = diffScore

print(bestResult)