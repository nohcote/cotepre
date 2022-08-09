# 1/1 (1/2 2/1) (3/1 2/2 1/3) (1/4 2/3 3/2 4/1) (5/1 4/2 3/3 2/4 1/5) ...
# 1, 2~3, 4~6, 7~10, 11~15, ...
# 1, 3, 6, 10, 15, ... -> n(n+1)/2
# range: i(i+1)/2 -i+1 ~ i(i+1)/2
# odd: i*(i+1)/2-num+1 ~ num-i*(i-1)/2, even: flip

def getnum(num):
    i = 1
    while i*(i+1)/2 < num:
        i += 1
    if i%2 == 1: # odd
        print("%d/%d" % (i*(i+1)/2-num+1, num-i*(i-1)/2))
    else: # even
        print("%d/%d" % (num-i*(i-1)/2, i*(i+1)/2-num+1))

N = int(input())
getnum(N)
