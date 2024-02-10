# ダイクストラ法
# sがスタート、nが頂点数
# ※ costの更新は実施隊対象に合わせて更新必要
# https://atcoder.jp/contests/abc325/submissions/46839996
# https://atcoder.jp/contests/abc325/submissions/46811569

from heapq import heappop, heappush, heapify
def dijkstra1(s,n):
    INF = 10**15
    dist = [INF]*(n+1)    # 距離
    que = [(0,s)]         # (cost, 頂点番号)
    dist[s] = 0
    while que:
        c,crr = heappop(que)                  # 探索対象のもののうち最もcostが低いものを選択
        if c > dist[crr]:                     # 既存のcostよりも大きい場合は無視
            continue
        for nxt in range(n):                  # 探索対象の頂点
            cost = D[crr][nxt] * A            # cost(ex.所用時間)の更新、ここは適宜調整
            if dist[crr] + cost < dist[nxt]:  # 既存のcostより小さいものが見つかった場合は更新
                dist[nxt] = dist[crr] + cost
                heappush(que,(dist[nxt],nxt))
    return dist

dijkstra1(1,N) # index 1~Nまで
