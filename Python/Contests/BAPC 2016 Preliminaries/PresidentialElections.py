import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################


def get_subsolution(entry):
    maxStateIndex, maxDelegateBoundary = entry
    if entry in subsolutions:
        return subsolutions[entry]
    if maxDelegateBoundary < 0:
        return float("-inf")
    if maxDelegateBoundary == 0:
        return 0
    if maxStateIndex < 0:
        return 0
    stateInfoForIndex = stateInfos[maxStateIndex]
    delegatesToEarn, votersToWin = stateInfoForIndex
    subsolution = max(get_subsolution((maxStateIndex-1, maxDelegateBoundary)), votersToWin +
                      get_subsolution((maxStateIndex-1, maxDelegateBoundary-delegatesToEarn)))
    subsolutions[entry] = subsolution
    return subsolution


nofStates = int(sys.stdin.readline().strip())
stateInfos = []
totalDelegates = 0
constituentDelegates = 0
federalDelegates = 0
totalVotersForKnapsack = 0
for _ in range(nofStates):
    nofDelegates, nofConstituents, nofFederals, nofUndecided = list(
        map(int, sys.stdin.readline().strip().split(' ')))
    totalDelegates += nofDelegates
    totalVotersForState = nofConstituents + nofFederals + nofUndecided
    boundaryForVoters = (totalVotersForState // 2) + 1
    if nofConstituents >= boundaryForVoters:
        constituentDelegates += nofDelegates
        continue
    elif nofFederals >= (boundaryForVoters if totalVotersForState % 2 == 1 else boundaryForVoters - 1):
        federalDelegates += nofDelegates
        continue
    votersToWinThisState = boundaryForVoters - nofConstituents
    totalVotersForKnapsack += votersToWinThisState
    stateInfo = (nofDelegates, votersToWinThisState)
    stateInfos.append(stateInfo)

boundaryForConstituentDelegates = (totalDelegates // 2) + 1
boundaryForFederalDelegates = boundaryForConstituentDelegates if totalDelegates % 2 == 1 else boundaryForConstituentDelegates - 1

if constituentDelegates >= boundaryForConstituentDelegates:
    print(0)
    exit()
if federalDelegates >= boundaryForFederalDelegates:
    print('impossible')
    exit()

necessaryConstituentDelegates = boundaryForConstituentDelegates - constituentDelegates
necessaryFederalDelegates = boundaryForFederalDelegates - federalDelegates

# ss[i][j] = the most voters won for Federates without getting more delegates than j using only states up until i
subsolutions = {}

resultForFederals = get_subsolution(
    (len(stateInfos) - 1, necessaryFederalDelegates - 1))

resultForConstituents = totalVotersForKnapsack - resultForFederals

print(resultForConstituents)
