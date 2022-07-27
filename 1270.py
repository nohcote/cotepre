import sys
from collections import Counter


n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    temparr = list(map(int, sys.stdin.readline().rstrip().split()))
    temparr2 = temparr[1:]
    tempkeys = list(dict.fromkeys(temparr2))
    tempcounter = Counter(temparr2)
    tempbool = False

    for t in tempkeys:
        if tempcounter[t] > temparr[0]/2:
            print(t)
            tempbool = True
            break
    if not tempbool:
        print("SYJKGW")