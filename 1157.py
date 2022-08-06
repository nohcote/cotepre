from collections import Counter

mc = Counter(input().upper()).most_common()
print(mc[0][0] if len(mc) == 1 or mc[0][1] != mc[1][1] else "?")