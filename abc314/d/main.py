#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] != "/Users/seigo"
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

N=int(input())
S=list(input())
Q=int(input())
TXC = []
for ii in range(Q):
    txc=list(map(str, input().split()))
    TXC.append(txc)
#error(TXC)

# N回の操作後に大文字/小文字はどちらになっているか(0:小文字,1:大文字)
TXC1 = []
latest = [-1,-1]
for ii in range(Q):
    txc = TXC[ii]
    if txc[0] == "1":
        TXC1.append((ii,txc))
    if txc[0] == "2":
        # 小文字
        latest = [ii,2]
    if txc[0] == "3":
        # 大文字
        latest = [ii,3]
error(latest)
error(TXC1)

# 基本的に全てlatestの操作を採用する
TXC1_pre = []
TXC1_post = []
for txc in TXC1:
    if txc[0] < latest[0]:
        TXC1_pre.append(txc[1])
    else:
        TXC1_post.append(txc[1])
error(TXC1_pre)
error(TXC1_post)

# pre処理
error(S)
for txc in TXC1_pre:
    error(txc)
    error(txc[2])
    idx = int(txc[1])
    S[idx-1] = txc[2]

# 全てlatestの操作を実施
for ii in range(N):
    if latest[1] == 2:
        S[ii] = S[ii].lower()
    if latest[1] == 3:
        S[ii] = S[ii].upper()
# post処理
for txc in TXC1_post:
    idx = int(txc[1])
    S[idx-1] = txc[2]
print("".join(S))
