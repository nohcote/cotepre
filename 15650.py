import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
arr = deque()

def dfs(limit):
    if len(arr) == M:
        [print(e, end=" ") for e in arr]
        print()
        return
    else:
        for i in range(1, N+1):
            if i not in arr and limit < i:
                arr.append(i)
                dfs(i)
                arr.pop()


dfs(0)
