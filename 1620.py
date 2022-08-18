import sys


N, M = map(int, sys.stdin.readline().split())
count = 1
pokedex = {}

for _ in range(N):
    temp = sys.stdin.readline().rstrip()
    pokedex[str(count)] = temp
    pokedex[temp] = str(count)
    count += 1

for e in [sys.stdin.readline().rstrip() for _ in range(M)]:
    print(pokedex[e])