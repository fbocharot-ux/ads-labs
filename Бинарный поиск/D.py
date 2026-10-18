a, b, c, d = map(float, input().split())

def f(x):
    return a * x**3 + b * x**2 + c * x + d

left, right = -2000.0, 2000.0

for _ in range(50):
    mid = (left + right) / 2
    if f(mid) * f(left) > 0:
        left = mid
    else:
        right = mid

print(f"{(left+right)/2:.10f}")