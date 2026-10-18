n, a, b, w, h = map(int, input().split())


def good(d):
    A = a + 2 * d
    B = b + 2 * d
    return (w // A) * (h // B) >= n or (w // B) * (h // A) >= n


left, right = 0, max(w, h)
while right - left > 1:
    mid = (left + right) // 2
    if good(mid):
        left = mid
    else:
        right = mid
print(left)
