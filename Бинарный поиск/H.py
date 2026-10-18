w, h, n = map(int, input().split())

def diplom_rast(X):
    return (X // w) * (X // h) >= n

left, right = 0, max(w, h) * n
while right - left > 1:
    mid = (left + right) // 2
    if diplom_rast(mid):
        right = mid
    else:
        left = mid
print(right)