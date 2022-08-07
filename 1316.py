N = int(input())
groupword = 0
for i in range(N):
    temp = input()
    # if len<=2, O
    if len(temp) <= 2:
        groupword += 1
    else:
        groupwordflag = True
        for j in range(len(temp)):
            if not groupwordflag:
                break
            checkflag = False
            for k in range(j+1, len(temp)):
                if checkflag:
                    if temp[k] == temp[j]:
                        groupwordflag = False
                        break
                elif temp[k] != temp[j]:
                    checkflag = True
        groupword += 1 if groupwordflag else 0
print(groupword)