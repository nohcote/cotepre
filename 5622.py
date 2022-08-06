arr = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

def getsec(char)->int:
    for x in arr:
        if char in x:
            return arr.index(x) + 3 # 1: 2sec
    return 11 # 0
print(sum([getsec(y) for y in input()]))