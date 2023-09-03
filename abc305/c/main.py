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

H,W=map(int, input().split())
HW = [list(input()) for h in range(H)] 

# a,b,c,dを求める
# a 左上x
# b 左上y
# c 右下x
# d 右下y

# a 左上x
a = 1000
b = 1000
c = 0
d = 0
for jj in range(H):
    for ii in range(W):
        # "#"を見つける
        tx = HW[jj][ii]
        if tx == "#":
            a = min(a,ii)
            b = min(b,jj)
            c = max(c,ii)
            d = max(d,jj)

error(a,b,c,d)
for jj in range(b,d+1):
    for ii in range(a,c+1):
        tx = HW[jj][ii]
        if tx == ".":
            print(jj+1,ii+1)
            exit()

