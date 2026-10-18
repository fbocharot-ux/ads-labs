n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]

def good(X):
    total = 0
    for L in a:
        total += L//X
        if total >= k:
            return True
    return total >= k

left, right = 0, max(a) + 1
while right - left > 1:
    mid = (left + right) // 2
    if good(mid):
        left = mid
    else:
        right = mid
print(left)