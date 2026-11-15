import heapq

n = int(input())
a = [int(input()) for _ in range(n)]
heap = []
for i in range(n):
    f = a[i]
    first_fish = max(1000 - f, 1)

    heapq.heappush(heap, (first_fish, i + 1, f))

cur_pos = 1
cur_time = 0
while heap:
    birth_time, aqua_idx, f = heapq.heappop(heap)

    dist = abs(aqua_idx - cur_pos)

    if cur_time + dist <= birth_time:

        cur_pos = aqua_idx
        cur_time = birth_time

        new_f = f + 1
        next_fish = max(1000 - new_f, 1)
        heapq.heappush(heap, (birth_time + next_fish, aqua_idx, new_f))
    else:
        print(birth_time)
        break
