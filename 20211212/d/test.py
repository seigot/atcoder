import sys
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)

# https://atcoder.jp/contests/abc231/submissions/27883602
#N, M = map(int, input().split())
#l = [list(map(int, input().split())) for l in range(M)]
#error(N, M)
#error(l)

from collections import defaultdict

class UnionFind():

    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.root[self.find(x)]

    def roots(self):
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        return len(self.roots())

    def group_members(self):
        group_members = defaultdict(list) 
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def judge():
    N, M = map(int, input().split())
    uf = UnionFind(N)
    C = [0] * (N+1)  # 人が条件に出てくる回数をカウント
    for _ in range(M):
        a, b = map(int, input().split())
        if uf.same(a, b):  # 閉路（ループ）がないか判定
            return False
        uf.unite(a, b)
        C[a] += 1
        C[b] += 1

    for i in range(1,N+1):
        if C[i] >= 3:  # 同時に3人以上と隣り合うことはできない
            return False
    return True


print("Yes" if judge() else "No")
