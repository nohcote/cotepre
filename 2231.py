N = int(input())
s = {}
val = -1
for i in range(1, N+1):
    s[i] = i+sum([int(s) for s in str(i)])
    if s[i] == N:
        val = i
        break
if val == -1:
    print(0)
else:
    print(val)