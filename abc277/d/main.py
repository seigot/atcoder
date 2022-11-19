#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,M=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

from collections import defaultdict
#n,m = map(int,input().split())
#l = list(map(int,input().split()))

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
 


# 1.島を見つける
# 2.島ごとの数値の総和を求める
# 3.島ごとの数値の総和の総和 - max(島ごとの数値の総和)

# 1.
d = defaultdict(int)
dsum = defaultdict(int)
A.sort()
for ii in range(N):
    a = A[ii]
    d[a] += 1

# 2.
#A.sort()
uf = UnionFind(N+1)
for i in range(0,N-1):
  if A[i] == A[i+1] or A[i]+1 == A[i+1]:
    uf.union(i,i+1)
if (A[N-1]+1)%M == A[0]:
    uf.union(N-1,0)

#print(A)
for i in range(N):
#    print(uf.find(targeti))
#    rootnum = uf.find(targeti)
    rootnum = uf.find(i)
#    print(i, rootnum, A[i])
    dsum[rootnum] += A[i]

# 3.
#print(dsum)
aa = dsum.values()
print(sum(aa)-max(aa))

