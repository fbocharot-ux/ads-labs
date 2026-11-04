def kruskal(edges):
    # 1. Сортируем рёбра по весу
    edges.sort(key=lambda x: x[2])

    # 2. Находим все уникальные вершины из рёбер
    vertices = {u for u, v, _ in edges} | {v for u, v, _ in edges}
    parent = {v: v for v in vertices}

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    mst = []
    total_weight = 0

    # 3. Набираем рёбра
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == len(vertices) - 1:
                break

    return mst, total_weight

from collections import defaultdict
import heapq


def prim(edges):
    if not edges:
        return [], 0

    # 1. Строим граф и считаем количество уникальных вершин
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((w, u, v))
        adj[v].append((w, v, u))

    total_vertices = len(adj)

    # 2. Стартуем с первой попавшейся вершины
    start_node = next(iter(adj))
    in_tree = {start_node}
    heap = list(adj[start_node])
    heapq.heapify(heap)

    mst = []
    total_weight = 0

    # 3. Тянем минимальные рёбра
    while heap and len(mst) < total_vertices - 1:
        w, u, v = heapq.heappop(heap)
        if v in in_tree:
            continue

        in_tree.add(v)
        mst.append((u, v, w))
        total_weight += w

        for edge in adj[v]:
            if edge[2] not in in_tree:
                heapq.heappush(heap, edge)

    return mst, total_weight