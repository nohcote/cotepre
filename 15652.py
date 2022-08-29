import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
arr = deque()

def dfs(begin):
    if len(arr) == M:
        print(*arr)
        return
    else:
        for i in range(begin, N+1):
            arr.append(i)
            dfs(i)
            arr.pop()


dfs(1)
