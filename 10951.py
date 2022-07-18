while True:
    try:
        a, b = list(map(int, input().split(" ")))
        if a > 0 and b > 0 and a < 10 and b < 10:
            print(a+b)
        else:
            break
    except:
        break