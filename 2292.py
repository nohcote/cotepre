# 1, 2~7, 8~19, 20~37, 38~61, ...
# 1, 6, 12, 18, 24, ...
num = int(input())

term = 6
pivot = 2
count = 2
if num == 1:
    print(1)
else:
    while True:
        if pivot <= num <= pivot + term - 1:
            print(count)
            break
        pivot += term
        term += 6
        count += 1
