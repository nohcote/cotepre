import sys


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, mul, div = map(int, sys.stdin.readline().split())
maxval = -sys.maxsize
minval = sys.maxsize


def dfs(level, val):
    global plus, minus, mul, div, maxval, minval
    
    if N == level:
        maxval = max(maxval, val)
        minval = min(minval, val)
        return
    if plus:
        plus -= 1
        dfs(level+1, val+A[level])
        plus += 1
    if minus:
        minus -= 1
        dfs(level+1, val-A[level])
        minus += 1
    if mul:
        mul -= 1
        dfs(level+1, val*A[level])
        mul += 1
    if div:
        div -= 1
        if val < 0:
            dfs(level+1, (-val)//A[level] * -1)
        else:
            dfs(level+1, val//A[level])        
        div += 1



dfs(1, A[0])

print(maxval)
print(minval)