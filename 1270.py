import sys
from collections import Counter


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    temparr = list(map(int, sys.stdin.readline().rstrip().split()))
    tempkeys = list(dict.fromkeys(temparr[1:]))
    tempcounter = Counter(temparr[1:])
    tempstr = "SYJKGW"
    for t in tempkeys:
        if tempcounter[t] > temparr[0]/2:
            tempstr = t
            break
    print(tempstr)
