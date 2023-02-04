##### UnionFind
# https://algo-method.com/descriptions/136
class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    # 根を求める
    def root(self, x):
        if self.par[x] == -1: return x # x が根の場合は x を返す
        else:
          self.par[x] = self.root(self.par[x]) # 経路圧縮
          return self.par[x]

    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] < self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する
        return True
    
    # x を含む根付き木のサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]

uf = UnionFind(N+1) # N: 頂点数



##### BFS
# https://algo-method.com/descriptions/114#h2-81
# 入力
N, M = map(int, input().split())
G = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())

    # 頂点 A から頂点 B への辺を張る
    G[A].append(B)
    G[B].append(A)

# 最初の頂点集合 (スタートは頂点 0 のみ)
nodes = [0]

# 各頂点が何手目に探索されたか
# -1 は「まだ探索されていない」ことを表す
dist = [-1] * N

# k 手目に探索された頂点集合を格納 (最大でも N-1 手まで)
nodes = [[] for i in range(N)]

# 頂点 0 を始点とする
dist[0] = 0
nodes[0] = [0]

# k 手目の探索をする
for k in range(1, N):
    # k-1 手目に探索された各頂点 v に対して
    for v in nodes[k - 1]:
        # 頂点 v から 1 手で行ける頂点 next_v を探索
        for next_v in G[v]:
            # 頂点 next_v が探索済みであれば何もしない
            if dist[next_v] != -1:
                continue

            # 頂点 next_v を探索する
            dist[next_v] = dist[v] + 1
            nodes[k].append(next_v)