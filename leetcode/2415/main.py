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
#from sortedcontainers import SortedSet, SortedList, SortedDict
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush, heapify
from math import gcd
from itertools import permutations,combinations,accumulate
from copy import deepcopy
dpos2 = ((1, 0), (0, 1))
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos4cross = ((1, 1), (1, -1), (-1, 1), (-1, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
def invmod(a): # 期待値の計算: X/Y % MOD = X * invmod(Y) % MOD
    return pow(a,-1,MOD)
def conv_2dto1d(h, w, W): # h:height, w:width, W:横幅
    return h * W + w
INF = float("inf")
MINF = -float("inf")

root = [2,3,5,8,13,21,34]
# 1 2-3 4-7 8-15 16-31 32-63
# 1 2   4   8    16
# idx = ii-1
# idx:idx+ii
# ii=1, 0:1
# ii=2, 1:3
# ii=4, 3:7
# ii=7, 7:15

ans = []
lenr = len(root)
ii = 1
mm = 0
while ii < lenr:
    idx = ii-1
    l = root[idx:idx+ii]
    ii *= 2
    if mm % 2 == 1:
        l = l[::-1]
    for v in l:
        ans.append(v)
    mm += 1
print(ans)