#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N, M, E=map(int, input().split())
UV = []
for ii in range(E):
    U, V=map(int, input().split())
    U -= 1
    V -= 1
    if U >= N: # 発電所はひとまとめ
        U = N
    if V >= N: # 発電所はひとまとめ
        V = N
    UV.append([U, V])
Q=int(input())
X = []
X_cnt = defaultdict(int)
for ii in range(Q):
    x = int(input())
    x -= 1
    X.append(x)
    X_cnt[x] = 1

exist_edge = []
for ii in range(E):
    if X_cnt[ii] == 0:
        exist_edge.append(UV[ii])
#print(exist_edge)

uf = UnionFind(N+1)
# 初期化
for ii in range(len(exist_edge)):
    a = exist_edge[ii][0]
    b = exist_edge[ii][1]
    #print(a,b)
    uf.union(a,b)
#print(N, uf.size(N))
#print(uf.members(N))

X_rev = X[::-1]
#print(X)
#print(X_rev)
#print(UV)
ans = []
for ii in range(len(X)):

    ans.append(uf.size(N)-1)
    #idx = (-1*ii -1
    idx = X_rev[ii]
    #print(ii, idx, UV[idx])
    #print(idx)
    a = UV[idx][0]
    b = UV[idx][1]
    uf.union(a,b)

print(*ans[::-1])
