def balls_count(T, Ti, Zi, Yi):
    cycle_full = Zi * Ti + Yi
    cycles = T // cycle_full
    ostat = T % cycle_full
    return cycles * Zi + min(Zi, ostat // Ti)


def good(T):
    total = 0
    for t, z, y in helpers:
        total += balls_count(T, t, z, y)
        if total >= M:
            return True
    return total >= M


M, N = map(int, input().split())
helpers = []
for _ in range(N):
    t, z, y = map(int, input().split())
    helpers.append((t, z, y))

left, right = -1, M * max(t * z + y for t, z, y in helpers) + 1
while right - left > 1:
    mid = (left + right) // 2
    if good(mid):
        right = mid
    else:
        left = mid
T = right
print(T)

counts = [balls_count(T, t, z, y) for t, z, y in helpers]
excess = sum(counts) - M
for i in range(N - 1, -1, -1):
    if excess <= 0:
        break
    cut = min(counts[i], excess)
    counts[i] -= cut
    excess -= cut

print(*counts)