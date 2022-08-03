from collections import Counter
print(len(Counter([i%42 for i in [int(input()) for _ in range(10)]]).keys()))