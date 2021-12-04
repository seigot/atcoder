#!/bin/python

n, m = map(int, input().split())
l = [list(map(int, input().split())) for l in range(m)]

# https://at274.hatenablog.com/entry/2018/02/02/173000
#class UnionFind:
#    def __init__(self, n):
#        self.par = [i for i in range(n+1)]
#        self.rank = [0] * (n+1)
#
#    # 検索
#    def find(self, x):
#        if self.par[x] == x:
#            return x
#        else:
#            self.par[x] = self.find(self.par[x])
#            return self.par[x]
#
#    # 併合
#    def union(self, x, y):
#        x = self.find(x)
#        y = self.find(y)
#        if self.rank[x] < self.rank[y]:
#            self.par[x] = y
#        else:
#            self.par[y] = x
#            if self.rank[x] == self.rank[y]:
#                self.rank[x] += 1
#
#    # 同じ集合に属するか判定
#    def same_check(self, x, y):
#        return self.find(x) == self.find(y)

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def same_check(self, x, y):
        return self.find(x) == self.find(y)
 
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if not self.same_check(x, y):
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if not self.same_check(x, y):
                self.size[x] += self.size[y]
                self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def size(self, x):
        x = self.find(x)
        return self.size[x]

N, M = map(int, input().split())
Edge = []
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    Edge.append((a, b))

Edge.sort(reverse=True)

UF = UnionFind(N)
Ans = [-1]*N
ans = 0
edge_cnt = 0

for now in range(N)[::-1]:
    ans += 1
    while edge_cnt < M and now <= Edge[edge_cnt][0]:
        if not UF.same_check(Edge[edge_cnt][0], Edge[edge_cnt][1]):
            ans -= 1
            UF.union(Edge[edge_cnt][0], Edge[edge_cnt][1])
        edge_cnt += 1
    Ans[now] = ans

for ans in Ans[1:]:
    print(ans)
print(0)

#
#UF=UnionFind(10)
#
#---
#print(UF.size(1))
# Nはノード数, Mは条件数(友達関係)
#N = 6
#M = 4
#
#UF = UnionFind(n) # ノード数で初期化
#for _ in range(M):
#    x, y = l[_] #inputmap() # 友達関係を取得(x=1,y=2)
#    UF.union(x-1, y-1) # 同じ集合にする (0-index)
# 
#print(UF.size(0)) # 1番目が属する集合の要素数を取得
