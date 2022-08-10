N = int(input())

temp = N
count = N // 5
N %= 5
while N % 3 != 0 and count > 0:
    N += 5
    count -= 1
if N%3 == 0:
    print(count+N//3)
else:
    print(-1)