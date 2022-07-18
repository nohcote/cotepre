import sys


n, m = list(map(int, sys.stdin.readline().rstrip().split()))

arr = [[], []]

for x in range(0, 2):
    for i in range(0, n):
        arr[x].append([])
        temparr = sys.stdin.readline().rstrip().split()
        for j in range(0, m):
            arr[x][i].append(temparr[j])
        
for i in range(0, n):
    for j in range(0, m):
        print(int(arr[0][i][j])+int(arr[1][i][j]), end=' ')
    print()