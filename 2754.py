import sys


score = 69

n = sys.stdin.readline().rstrip()
if '+' in n:
    score += 0.3
elif '-' in n:
    score -= 0.3
    
print("%.1f" % (score - ord(n[0])) if score - ord(n[0]) > 0 else 0.0)