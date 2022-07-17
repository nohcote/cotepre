while True:
    inp = input().split(" ")
    if int(inp[0]) == 0:
        break
    else:
        print(int(inp[0]) + int(inp[1]))