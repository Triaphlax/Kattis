import sys
import math

###############################
sys.stdin = open('TEST/Brexit_Test.txt', 'r')
###############################

class Node:
    def __init__(self, number):
        self.number = number
        self.partners = {}
        self.nofInitialPartners = -1
        self.nofCurrentPartners = -1
        self.inEU = True
        self.wantsToLeave = False

    def addPartner(self, partner):
        self.partners[partner] = True

    def finalizeNode(self):
        self.nofInitialPartners = len(self.partners)
        self.nofCurrentPartners = len(self.partners)
    
    def removePartner(self, partner):
        self.partners[partner] = False
        self.nofCurrentPartners -= 1
        if self.nofInitialPartners - self.nofCurrentPartners >= math.ceil(self.nofInitialPartners / 2) and not self.wantsToLeave:
            self.wantsToLeave = True

    def leave(self):
        self.inEU = False


settings = list(map(int, sys.stdin.readline().strip().split(' ')))
nofCountries = settings[0]
nofTradingPartnerships = settings[1]
homeCountry = settings[2]
firstCountryToLeave = settings[3]

nodeDict = {}

for country in range(1, nofCountries+1): # countries are 1-indexed
    nodeDict[country] = Node(country)

for _ in range(nofTradingPartnerships):
    partnershipSettings = list(map(int, sys.stdin.readline().strip().split(' ')))
    node1 = nodeDict[partnershipSettings[0]]
    node2 = nodeDict[partnershipSettings[1]]
    node1.addPartner(node2.number)
    node2.addPartner(node1.number)

for node in nodeDict.values():
    node.finalizeNode()

stack = [firstCountryToLeave]
nodeDict[firstCountryToLeave].wantsToLeave = True
while stack:
    currentCountryNumber = stack.pop(0)
    currentCountryNode = nodeDict[currentCountryNumber]
    if not currentCountryNode.inEU:
        continue
    for partnerNumber, isStillPartner in currentCountryNode.partners.items():
        if isStillPartner:
            partnerNode = nodeDict[partnerNumber]
            partnerNode.removePartner(currentCountryNumber)
            currentCountryNode.removePartner(partnerNumber)
            if partnerNode.wantsToLeave:
                stack.append(partnerNode.number)
    currentCountryNode.leave()

homeNode = nodeDict[homeCountry]
if homeNode.inEU:
    print('stay')
else:
    print('leave')