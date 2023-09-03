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

#https://atcoder.jp/contests/abc314/submissions/44517157 
import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
C = []
P = []
S = []
Z = []
for i in range(N):
    line = list(map(int, input().split()))
    C.append(line[0])
    P.append(line[1])
    S.append(sorted(line[2:]))

for s in S:
    zero = 0
    for si in s:
        zero += int(si == 0)
    # i番目のスロットの0が出る確率
    Z.append(zero / len(s))


INF = 10**18
dp = [INF] * (M + 1)
dp[M] = 0

for m in reversed(range(M)):
    best_e = INF
    # 各スロットについて考える
    for c, p, s, z in zip(C, P, S, Z):
        e = 0
        # 該当スロットの出目の期待値を求める
        for si in s:
            if si != 0:
                # 0以外の場合はdp+cを足す(eになる期待値+c(逆順なのでこれでOK))
                e += dp[min(M, m + si)] + c
            else:
                # 0の場合はcを足す(もう一度実施するため)
                e += c
#        e = e / ((1 - z) * p)
        e *= 1/(p * (1 - z))  # 0以外が出現する回数で割る

        if best_e > e:
            best_e = e

    dp[m] = best_e

print(dp[0])


"""
ある状態でルーレットを選ぶ時、
最も期待値が小さいものを選ぶ
"""
