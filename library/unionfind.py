# アルゴ式
# https://algo-method.com/descriptions/136
# 過去問
# https://github.com/seigot/atcoder/blob/71ad3ec67c9895b38c265ca4c2ed4d9310179bb9/abc288/c/main.py
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

uf = UnionFind(N+1)

# https://atcoder.jp/contests/abc334/submissions/48806634
# UnionFind
# N: nodeの個数
class UnionFind:
    def __init__(self, N):
        self.N = N
        self.parent_or_size = [-1] * N # parentを返す
        self.group_count = N  # groupの個数を返す

    def root(self, x):        # rootを返す
        if self.parent_or_size[x] < 0:
            return x
        else:
            self.parent_or_size[x] = self.root(self.parent_or_size[x])
            return self.parent_or_size[x]

    def unite(self, x, y):    # x,yを同じグループに所属させる
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        if -self.parent_or_size[root_x] < -self.parent_or_size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent_or_size[root_x] += self.parent_or_size[root_y]
        self.parent_or_size[root_y] = root_x
        self.group_count -= 1

    def same(self, x, y):     # x,yが同じグループかどうかを判定する
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent_or_size[self.root(x)]

    def groups(self):         # groupsリストを返す
        ret = defaultdict(list)
        for i in range(self.N):
            ret[self.root(i)].append(i)
        return [group for group in ret.values()]

uf = UnionFind(H * W + 1) # nodeの個数、"その他"みたいなのを用意したい場合は+1加える
base = uf.group_count     # "#"のグループをカウントする
uf.unite(x, y)            # x,yを同じグループにする
uf.root(x)                # xのrootを求める
