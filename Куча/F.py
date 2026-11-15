import heapq

n = int(input())

cargos = []
for _ in range(n):
    t, l = map(int, input().split())
    cargos.append((t, t + l))

cargos.sort(key=lambda x: x[0])

end_times_heap = []
max_machines = 0
for start, end in cargos:
    while end_times_heap and end_times_heap[0] <= start:
        heapq.heappop(end_times_heap)
    heapq.heappush(end_times_heap, end)
    if len(end_times_heap) > max_machines:
        max_machines = len(end_times_heap)

print(max_machines)
