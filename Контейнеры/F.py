from collections import deque

N, K = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()
res = []

for i in range(N):
    while dq and arr[dq[-1]] >= arr[i]:
        dq.pop()
    dq.append(i)

    if dq[0] <= i - K:
        dq.popleft()

    if i >= K - 1:
        res.append(arr[dq[0]])

print('\n'.join(map(str, res)))
