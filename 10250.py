for i in range(int(input())):
    h, w, n = map(int, input().split()) # height, room amount, nth guest
    # YY = n % h
    # XX = n // h + 1
    # 1~6, 7~12, 13~18, ...
    # 0~5, 6~11, 12~17, ... +1
    if h * w < n:
        continue
    print(f"{(n-1)%h +1}{str((n-1)//h +1).zfill(2)}")