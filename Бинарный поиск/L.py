N, R, C = map(int, input().split())
a = sorted(int(input()) for _ in range(N))

def good(d):
    count = 0
    i = 0
    while i + C <= N:
        if a[i + C - 1] - a[i] <= d:
            count += 1
            i += C
        else:
            i += 1
    return count >= R

left, right = -1, a[-1] - a[0]
while right - left > 1:
    mid = (left + right) // 2
    if good(mid):
        right = mid
    else:
        left = mid
print(right)