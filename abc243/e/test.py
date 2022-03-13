N, M = map(int, input().split()) #N頂点,M辺
es = []
inf = 10**18
for _ in range(M):
    # 頂点A, 頂点B, 距離を0indexで読み込む
    a, b, c = map(int, input().split())
    es.append((a - 1, b - 1, c))

# 距離を求める
d = [[inf] * N for _ in range(N)]
for a, b, c in es:
    d[a][b] = c # AB間の距離
    d[b][a] = c # BA間の距離

# これがワーシャルフロイド法?
# 最短路を計算する
for k in range(N):         # 中継点
    for i in range(N):     # 頂点の距離を計算する
        for j in range(N): # 頂点の距離を計算する
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
answer = 0
for a, b, c in es:
    unused = 0
    for i in range(N):
        # 他にも頂点間の最短路があるか探す
        # 他の頂点を経由した方が最短路であるならば該当の辺は削除可能
        if d[a][i] + d[i][b] <= c:
            unused = 1
    answer += unused

print(answer)
