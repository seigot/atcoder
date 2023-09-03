#!/usr/bin/env python3                                                                          
import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(4100000)
import math
import os
from inspect import currentframe
ONLINE_JUDGE = os.environ["HOME"] == "/home/runner"
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

from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

places = defaultdict(list)
for i, a in enumerate(A):
    # aのindexを記憶
    places[a].append(i)

# 数ごとに計算する
ans = 0
for line in places.values():
    error(line)
    prev = 0 #line[0] - 1 # 初期化
    nline = len(line)
    for j, i in enumerate(line):
#        total += j * (i - prev - 1) # (prevの選択肢)*(間に存在する数)
        total = 0
        total += j * (nline-j) * (i - prev - 1) # (prevの選択肢)*(間に存在する数)
        prev = i
        error(j,i,total)
        ans += total

print(ans)

