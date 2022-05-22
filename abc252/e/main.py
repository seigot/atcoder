"""
ダイクストラ法使用:(M+N)logN
プリム法:(V+E)logV
"""

import heapq
n, m = map(int, input().split())

# 道路の数を整理する(街と、道路およびコストを管理する)
edge = [[] for _ in range(n+1)]
for i in range(1, m+1):
    a, b, c = map(int, input().split())
    edge[a].append((c, b, i))
    edge[b].append((c, a, i))

edges = [(0, 1, 0)] # 探索初期値
tree_edge = []      # 答えとなるedgeの番号
is_check = [False] * (n+1) # N番目の街を探索済かどうか
is_check[1] = True  # 初期化(1番目の街は探索済)

# 1つ目の街とつながる道を対象とする
for n_cost, n_vertex, n_i in edge[1]:
    heapq.heappush(edges, (n_cost, n_vertex, n_i))

# ダイクストラ法で求める
# 各都市に到達する直前の道路を記録する
while edges:
    cost, vertex, i = heapq.heappop(edges)
    if is_check[vertex]:
        # 次の街を探索済であればスキップ
        continue
    tree_edge.append(i)
    # vertexの街から繋がる街を探索する
    is_check[vertex] = True
    for n_cost, n_vertex, n_i in edge[vertex]:
        if is_check[n_vertex]:
            # 探索済であればスキップ
            continue
        heapq.heappush(edges, (cost + n_cost, n_vertex, n_i))
print(*tree_edge)
