n, k = map(int, input().split())
a = list(map(int, input().split()))

def distance(d):
    count = 1
    last = a[0]
    for x in a[1:]:
        if x - last >= d:
            count += 1
            last = x
    return count >= k

left, right = 1, a[-1] - a[0] + 1
while right - left > 1:
    mid = (left + right) // 2
    if distance(mid):
        left = mid
    else:
        right = mid
print(left)