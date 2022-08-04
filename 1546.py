input()
arr = list(map(int, input().split()))
M = max(arr)
print(sum(arr)/M*100/len(arr))