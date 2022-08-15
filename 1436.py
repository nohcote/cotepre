import sys


num = int(input())
count = 0
for i in range(sys.maxsize):
    if "666" in str(i):
        count += 1
    if count == num:
        print(i)
        break