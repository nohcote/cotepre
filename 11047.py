import sys
from collections import deque


input = sys.stdin.readline
N, K = map(int, input().split())
coins = deque()
[coins.append(int(input())) for _ in range(N)]
coins = sorted(coins, reverse=True)
mincount = 0

for i in range(N):
    mincount += K // coins[i]
    K %= coins[i]

print(mincount)