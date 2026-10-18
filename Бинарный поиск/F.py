n, x, y = map(int, input().split())

quick = min(x, y)
slow  = max(x, y)

def min_time(T):
    return T // quick + T // slow >= n-1

left, right = 0, (n - 1) * slow
while right - left > 1:
    mid = (left + right) // 2
    if min_time(mid):
        right = mid
    else:
        left = mid

print(quick + right)