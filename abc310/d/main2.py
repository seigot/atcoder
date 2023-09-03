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

n,t,m = map(int,input().split())
hate = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    hate[a-1] |= 1<<(b-1)  # hateをbit情報で管理(たかだかMax10名なので大丈夫)
    hate[b-1] |= 1<<(a-1)  # hateをbit情報で管理(たかだかMax10名なので大丈夫) 

# dp[S][t]:=(S に含まれる選手を、互いに相性の悪い選手を含まないtチームに分ける場合の数)) 
dp = [[0]*(t+1) for i in range(1<<n)]
dp[0][0] = 1
for i in range(1<<n):       # ベースとなる組み合わせを全探索(人Aが同時にいる事の組み合わせ)
    for j in range(1,1<<n): # 追加となる組み合わせを全探索
        # 重複するケースはskip
        # (既に追加済みの人を追加しようとしても正しく更新ができないのでそもそも除く)
        if i&j != 0: continue 
        # 仲が悪いケースはskip
        # 追加対象のbit(追加対象のbitが立っている)において、hateのkbitと一致するケース
        ok = 1    # flag
        for k in range(n):
            if (j>> k) & 1 and hate[k] & j != 0:
                ok = 0
        if ok == 0: continue
        # 更新する
        for cnt in range(1,t+1):
            # チーム分け(1~tチームに分ける)
            # i+jを追加する場合、既存の組み合わせの情報を受け取る
            dp[i|j][cnt] += dp[i][cnt-1]

# 重複を除外する
d = 1
for i in range(t):
    d *= i+1
# 全員(集合S)を、Tチームに分ける//重複を除外
print(dp[-1][-1]//d)