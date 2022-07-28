import sys

resultsUnderFive = {
    1: '1',
    2: '2',
    3: '6',
    4: '4'
}
numberOfCases = int(sys.stdin.readline())
for case in range(0, numberOfCases):
    number = int(sys.stdin.readline())
    if number >= 5:
        print('0')
    else:
        result = resultsUnderFive[number]
        print(result)
