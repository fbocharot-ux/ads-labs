def line(L):
    cnt = 0
    for x in a:
        cnt += x // L
    return cnt >= k


n, k = map(int, input().split())
a = list()
for _ in range(n):
    a.append(int(input()))

left, right = 0, 10 ** 7 + 1
while right - left > 1:
    mid = (left + right) // 2
    if line(mid):
        left = mid
    else:
        right = mid
print(left)
