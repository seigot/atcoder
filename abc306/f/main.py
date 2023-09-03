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
from heapq import heappop, heappush
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

class FenwickTree:
    # フェニック木
    # 部分和の計算と要素の更新の両方を効率的に行える木構造である
    def __init__(self, n, init_data=0): 
        # 初期化
        # n : 要素数
        # init_data : 初期値
        self.size = n
        self.tree = [0] * (n + 1)
        if init_data != 0:
            for i in range(1, n + 1):
                self.add(i, init_data)

    def sum(self, i):
        # i番目までの和を求める
        ret = 0
        i += 1
        while i > 0:
            ret += self.tree[i]
            i -= i & -i
        return ret

    def add(self, i, x):
        # i番目までの要素にxを足す
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    def get(self, i):
        # i番目の要素を返す
        return self.sum(i) - self.sum(i - 1)

    def lower_bound(self, w):
        # wの境界を知る
        if w <= 0:
            return 0
        x = 0
        r = 1
        while r < self.size:
            r = r << 1
        length = r
        while length > 0:
            if length + x < self.size and self.tree[x + length] < w:
                w -= self.tree[x + length]
                x += length
            length = length >> 1
        return x

    def show(self):
        # print
        ret = []
        for i in range(self.size):
            ret.append(self.get(i))
        print(*ret)


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
V = []
for h in range(N):
    for w in range(M):
        V.append((A[h][w], h))
V.sort()
error(V) # (値、Si) の順にソート

count = [0] * N
ft = FenwickTree(N)
ans = int((1+M)*(M/2) * N*(N-1)/2) # 1~Mの和 × nC2通りの組み合わせ を計算
# 各数値の貢献度を加算していく（主客転倒）
for (a, h) in V:
    ft.add(h, 1)
    # 現在着目しているh(Si)よりも大きい値がすでにある場合は+1貢献するので加算する
    # 部分和はFenwickTreeを利用して高速に計算する
    # 問題となっている組み合わせ上、自分より大きい番号の集合が、
    # 今の値より小さい値をどれくらい持っているのかを考慮すれば良いため、以下の式でOK。
    ans += (ft.sum(N - 1) - ft.sum(h))
print(ans)
