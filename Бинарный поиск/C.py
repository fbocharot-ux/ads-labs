import math

C = float(input())

left = 0.0
right = max(1.0, C)

for _ in range(100):
    mid = (left + right) / 2
    if mid * mid + math.sqrt(mid) < C:
        left = mid
    else:
        right = mid

print(mid)