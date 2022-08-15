N, M = map(int, input().split())

arr = []
[arr.append([s for s in input()]) for _ in range(N)]

#find 8x8
mincountlist = []
for a in range(N-8+1):
    for b in range(M-8+1):
        white = black = 0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if arr[i][j] != 'W':
                        white += 1
                    if arr[i][j] != 'B':
                        black += 1
                else:
                    if arr[i][j] != 'B':
                        white += 1
                    if arr[i][j] != 'W':
                        black += 1
        mincountlist.append(white)
        mincountlist.append(black)
if mincountlist == []:
    print(0)
else:
    print(min(mincountlist))