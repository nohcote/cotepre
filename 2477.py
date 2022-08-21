import sys


K = int(sys.stdin.readline())
width = []
height = []
arr = []
for _ in range(6):
    arrow, amount = map(int, sys.stdin.readline().split())
    arr.append(amount)
    if arrow % 2 == 0:
        amount *= -1
    if arrow <= 2: # EW
        width.append(amount)
    else: # SN
        height.append(amount)

# bigrect
maxwidth = max([abs(e) for e in width])
maxheight = max([abs(e) for e in height])
bigrect = maxwidth * maxheight

# smallrect
smallrect_xyi = [e%6 for e in [arr.index(maxwidth)+3, arr.index(maxheight)+3]]
smallrect = arr[smallrect_xyi[0]] * arr[smallrect_xyi[1]]

# result = (bigrect - smallrect) * K
print(K*(bigrect-smallrect))
