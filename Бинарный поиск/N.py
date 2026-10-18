A, K, B, M, X = map(int, input().split())

def good(T):
    dmitry = A * (T - T // K)
    fedor  = B * (T - T // M)
    return dmitry + fedor >= X

left, right = 0, 2 * X + 1
while right - left > 1:
    mid = (left + right) // 2
    if good(mid):
        right = mid
    else:
        left = mid
print(right)