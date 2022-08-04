N = int(input())
arr = [input() for _ in range(N)]
score = 0
for item in arr:
    tempnum = 1
    for c in item:
        if c == "O":
            score += tempnum
            tempnum += 1
        else:
            tempnum = 1
    print(score)
    score = 0