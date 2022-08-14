import sys


moduloTerm = 1000000007
nofCases = int(sys.stdin.readline().strip())

for case in range(nofCases):
    d = int(sys.stdin.readline().strip())
    nineTodMinusOne = pow(9, d-1, moduloTerm)
    nineTod = (nineTodMinusOne * 9)  % moduloTerm
    result = (nineTod - nineTodMinusOne) % moduloTerm
    print(result)
