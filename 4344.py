import sys


for _ in range(int(sys.stdin.readline())):
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    criteria = sum(arr[1:])/arr[0]
    biggercount = len([i for i in arr[1:] if i > criteria])
    print("{:.3f}%".format(biggercount/arr[0]*100))
