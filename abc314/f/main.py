#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/contestant"
def error1(*args, end="\n"): # 変数のみ表示
    if ONLINE_JUDGE: return
    print("[stderr]", *args, end=end, file=sys.stderr)
def error(*args): # 変数の名前と値をまとめて表示
    if ONLINE_JUDGE: return
    names = {id(v): k for k, v in currentframe().f_back.f_locals.items()}
    print("[stderr]",' '.join([names.get(id(arg), '???') + ' = ' + repr(arg) for arg in args]), file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from math import gcd
from itertools import permutations,combinations
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a):
    return pow(a,-1,MOD)
INF = float("inf")
MINF = -float("inf")

#https://atcoder.jp/contests/ABC314/tasks/ABC314_f 
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd

from collections import defaultdict

class UnionFind:
    # n: nodeの数
    # 各nodeの親、ただしrootの場合はgroupのnode数*-1を格納する
    def __init__(self, n):
        self.n = n 
        self.p = [-1] * (n+1)

    # rootを探す
    def find(self, x): 
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    # 結合
    def union(self, x, y): 
        x = self.find(x) # rootを探す
        y = self.find(y) # rootを探す
        if x == y:
            return
        # rootが異なる場合は結合する
        # rootのp[x]は、
        if self.p[x] > self.p[y]:
            x, y = y, x
        self.p[x] += self.p[y]
        self.p[y] = x

    def same(self, a, b):
        return self.find(a) == self.find(b)

    def group(self):
        d = defaultdict(list)
        for i in range(1, self.n+1):
            par = self.find(i)
            d[par].append(i)
        return d

n = int(input())

uf = UnionFind(n+1)
ans = [0]*(n+1)
l = []
for i in range(n-1): # (n-1)回の試合がある
    a,b = map(int,input().split())
    pa = uf.find(a)
    pb = uf.find(b)
    # 自身の番号、自身の所属グループに所属している人の数を保存しておく
#    error("---")
#    error(a,pa,uf.p)
#    error(b,pb,uf.p)
#    error(uf.p[pa])
#    error(uf.p[pb])
    l.append([pa,pb,-uf.p[pa], -uf.p[pb]])
    # 結合
    uf.union(a,b)
#   error(uf.p[pa],uf.p)
#    error(uf.p[pb],uf.p)
#error(l)

mod = 998244353
# 確率を計算したテーブルを用意しておく
ba = [pow(i,mod-2, mod) for i in range(n+10)]
#error(ba)
for i in range(n-1)[::-1]: # (n-1)回の試合がある、これを逆順に計算する
#    error(i)
    a,b,c,d = l[i]
    ans[a] = max(ans[a], ans[b]) # 元々誰かが所属しているチーム1つの期待値しか計算していなかったので、それを参照する
    ans[b] = max(ans[a], ans[b]) # 同上
    ans[a] += c*ba[c+d] # 確率の期待値計算
    ans[b] += d*ba[c+d] # 確率の期待値計算 
    ans[a] %= mod
    ans[b] %= mod
print(*ans[1:])
