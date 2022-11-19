#!/usr/bin/env python3
from re import A
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N = int(input())
sx, sy, tx, ty = map(int,input().split())
xyr = []
for i in range(N):
    x, y, r = map(int, (input().split()))
    xyr.append([x, y, r])
#print(xyr)

# N=3000,N**2は9*10**6程であり全探索が可能と思われる
# 円が重なるかどうかチェックを全探索する
# 連結判定はUnion-Findを使用する
from collections import defaultdict

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
uf = UnionFind(N)

for ii in range(N):
    bx = xyr[ii][0]
    by = xyr[ii][1]
    br = xyr[ii][2]
    for jj in range(N):
        bbx = xyr[jj][0]
        bby = xyr[jj][1]
        bbr = xyr[jj][2]

        d = (bx-bbx)**2+(by-bby)**2
        #if d <= br + bbr:
        #print(ii,jj,d)
        if d == (abs(br - bbr))**2 or d == (br + bbr)**2 or ((abs(br-bbr))**2<d and d<(br+bbr)**2):
            # 内接している、外接している、交わっている
            # 重なっている
            # Union-Find
            uf.union(ii,jj)
        else:
            # 重なっていない
            pass

#print(uf.group_count())
#print(uf.same(1,2))
#print(sx, sy, tx, ty)
# sx, sy, tx, ty のindexを探す
s_idx=-1
t_idx=-1
for ii in range(N):
    
    # s
    d = (sx - xyr[ii][0])**2 + (sy - xyr[ii][1])**2
    if d == xyr[ii][2]**2:
        s_idx = ii
    # t
    d = (tx - xyr[ii][0])**2 + (ty - xyr[ii][1])**2
    if d == xyr[ii][2]**2:
        t_idx = ii

#print(s_idx, t_idx)
if uf.same(s_idx, t_idx):
    print("Yes")
else:
    print("No")