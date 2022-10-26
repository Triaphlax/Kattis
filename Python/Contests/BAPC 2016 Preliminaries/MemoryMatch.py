import sys

#############################
sys.stdin = open('TEST/TestFile.txt', 'r')
#############################

nofCards = int(sys.stdin.readline().strip())
nofMoves = int(sys.stdin.readline().strip())

cardSeen = [False] * (nofCards+1)
nofCardsUnseen = nofCards
symbolsSeen = {}
nofSymbolsSeen = 0
knownTwos = 0
knownOnes = 0
for _ in range(nofMoves):
    card1, card2, symbol1, symbol2 = list(
        sys.stdin.readline().strip().split(' '))
    card1 = int(card1)
    card2 = int(card2)

    card1Seen = cardSeen[card1]
    if not card1Seen:
        cardSeen[card1] = True
        nofCardsUnseen -= 1

    card2Seen = cardSeen[card2]
    if not card2Seen:
        cardSeen[card2] = True
        nofCardsUnseen -= 1

    if symbol1 in symbolsSeen:
        cards1 = symbolsSeen[symbol1]
        if len(cards1) == 1 and cards1[0] != card1:
            symbolsSeen[symbol1].append(card1)
            knownOnes -= 1
            knownTwos += 1
    else:
        nofSymbolsSeen += 1
        symbolsSeen[symbol1] = [card1]
        knownOnes += 1

    if symbol2 in symbolsSeen:
        cards2 = symbolsSeen[symbol2]
        if len(cards2) == 1 and cards2[0] != card2:
            symbolsSeen[symbol2].append(card2)
            knownOnes -= 1
            knownTwos += 1
    else:
        nofSymbolsSeen += 1
        symbolsSeen[symbol2] = [card2]
        knownOnes += 1

    if symbol1 == symbol2:
        knownTwos -= 1

pairsPossible = 0

# pick up known twos
pairsPossible += knownTwos

# pick up known ones
if nofCardsUnseen == knownOnes:
    pairsPossible += knownOnes
    nofCardsUnseen -= knownOnes

# pick up blind twos
elif nofCardsUnseen == 2:
    pairsPossible += 1
    nofCardsUnseen -= 2

print(pairsPossible)

# To test:
# - End with four known ones, with 4 cards remaining [4]
# - End with all 6 cards turned over, but no matches having been made [3]
# - End with two known pairs of two [2]
# - End with one unknown pair of two
#   - Because all other cards have been matched  [1]
#   - Because the other cards are matched or known pairs of two [1 + knownTwos]
# - End with two unknown pairs of two
#   - Because all other cards have been matched  [0]
#   - Because the other cards are matched or known pairs of two [0 + knownTwos]
# - End with two unknown pairs of one and an unknown pair of two [0]
