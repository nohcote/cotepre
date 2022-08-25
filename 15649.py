import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
arr = deque()

def dfs():
    if len(arr) == M:
        [print(e, end=" ") for e in arr]
        print()
        return
    else:
        for i in range(1, N+1):
            if i not in arr:
                arr.append(i)
                dfs()
                arr.pop()


dfs()