N = int(input())
warr = []
harr = []
for _ in range(N):
    x, y = map(int, input().split())
    warr.append(x)
    harr.append(y)

for a in zip(warr, harr):
    rank = 1
    for b in zip(warr, harr):
        if a[0]<b[0] and a[1]<b[1]:
            rank += 1
    print(rank, end=" ")
'''
warr_s = sorted(warr, reverse=True)
harr_s = sorted(harr, reverse=True)
warr_r = [warr_s.index(value)+1 for value in warr]
harr_r = [harr_s.index(value)+1 for value in harr]
rankarr = []

beforerank = 0
for a, b in zip(warr_r, harr_r):
    if a != b:
        beforerank = min(a,b)
        rankarr.append(beforerank)
    else:
        beforerank = a
        rankarr.append(a)
for r in rankarr:
    print(r, end=" ")
'''