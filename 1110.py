import sys



num = sys.stdin.readline().rstrip()
orignum = num
i = 0
while True:
    i += 1
    num = "".join([num[-1], str(sum([int(i) for i in list(num)]))[-1]])
    if int(num) != int(orignum): continue
    break
print(i)