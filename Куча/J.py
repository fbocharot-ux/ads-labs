import heapq

data = open(0).read().split()
if data:
    n = int(data[0])
    w = int(data[1])

    figs = []
    idx = 2
    for i in range(1, n + 1):
        a = int(data[idx])
        width = int(data[idx + 1])
        idx += 2
        figs.append((a, a + width - 1, i))

    figs.sort(key=lambda x: x[0])

    busy = []
    layers = []

    for left, right, fig_id in figs:
        if busy and busy[0][0] < left:
            _, lvl = heapq.heappop(busy)
        else:
            lvl = len(layers)
            layers.append([])
        layers[lvl].append(fig_id)
        heapq.heappush(busy, (right, lvl))

    print(len(layers))
    res = []
    for layer in layers:
        res.extend(layer)
    print(*res)
