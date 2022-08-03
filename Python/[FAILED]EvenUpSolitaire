import sys

class Node:
    def __init__(self, Size, CardParity, Backwards, Forwards):
        self.Size = Size
        self.SizeParity = Size % 2
        self.CardParity = CardParity
        self.Backwards = Backwards
        self.Forwards = Forwards

    def CombineWithForwardsNodeIfPossible(self):
        otherNode = self.Forwards
        if otherNode != None and self.CardParity == otherNode.CardParity:
            self.Size += otherNode.Size
            self.SizeParity = self.Size % 2
            self.Forwards = otherNode.Forwards
            return True
        return False


class LinkedList:
    def __init__(self, Head):
        self.Head = Head



nofCards = int(sys.stdin.readline())
parityCardLine = list(map(lambda x: int(x) % 2, sys.stdin.readline().split(' ')))


currentParity = -1
switches = -1
cardsAdjacentWithSameParity = 0
groupParityLine = []
ll = None
lastNode = None
for card in range(nofCards + 1):
    if card == nofCards or currentParity != parityCardLine[card]:
        switches += 1
        if switches > 0:
            groupParityLine.append(cardsAdjacentWithSameParity % 2)
            node = Node(cardsAdjacentWithSameParity, currentParity, lastNode, None)
            if ll == None:
                ll = LinkedList(node)
            if lastNode != None:
                lastNode.Forwards = node
            lastNode = node
        if card != nofCards:
            cardsAdjacentWithSameParity = 1
            currentParity = parityCardLine[card]
    else:
        cardsAdjacentWithSameParity += 1


while True:
    changes = 0
    currentNode = ll.Head
    while currentNode != None:
        if currentNode.Backwards == None and currentNode.Forwards == None:
            break
        if currentNode.CombineWithForwardsNodeIfPossible():
            changes += 1
        if currentNode.SizeParity == 0:
            if currentNode.Backwards != None:
                currentNode.Backwards.Forwards = currentNode.Forwards
            if currentNode.Forwards != None:
                currentNode.Forwards.Backwards = currentNode.Backwards
            changes += 1
        currentNode = currentNode.Forwards

    if changes == 0:
        break

remainingCards = 0
currentNode = ll.Head
while currentNode != None:
    remainingCards += currentNode.SizeParity
    currentNode = currentNode.Forwards

print(remainingCards)