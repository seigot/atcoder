from heapq import heappush, heappop,heapify
from collections import defaultdict

N, M, K = map(int, input().split())
gh = defaultdict(list)
for _ in range(M):
    u, v, a = map(int, input().split())
    gh[u].append((v, a))
    gh[v].append((u, a))

switchs = set(list(map(lambda x: int(x), input().split())))

# 各頂点の状態として、(距離、頂点、switchの状態)を持つ
# bfsで移動する際に以下のパターンを考える
#    - switchを押すパターン
#    - 移動するパターン
# heapqで探索の優先度を管理して優先度が高い（距離が短い）ものから探索を行う

q = [(0, 1, 1)]
heapify(q)
used = set()
while q:
    cost, v, s = heappop(q)

    if v == N:
        print(cost)
        exit(0)

    if (v, s) in used: continue
    used.add((v, s))

    # switchを押すパターン
    if v in switchs:
        if (v, s^1) not in used:
            # queueの先頭付近に加える
            heappush(q, (cost, v, s^1))
    # 移動するパターン
    for ii in gh[v]:
        to = ii[0]
        st = ii[1]
        if s != st:
            continue
        heappush(q, (cost+1, to, s))

print(-1)
