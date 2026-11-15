import heapq

heap = []
for line in open(0):
    parts = line.split()
    cmd = parts[0]
    if cmd == 'CLEAR':
        heap.clear()
    elif cmd == 'ADD':
        n = int(parts[1])
        heapq.heappush(heap, -n)
    elif cmd == 'EXTRACT':
        if not heap:
            print("CANNOT")
        else:
            print(-heapq.heappop(heap))
