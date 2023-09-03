#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline
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
def lcm(a, b):
    # 最小公倍数
    return a * b / gcd(a, b)

N=int(input())
XY=[list(map(int, input().split())) for n in range(N)]
error(XY)
s = set()
for ii in range(N):
    x1 = XY[ii][1]
    y1 = XY[ii][0]
    for jj in range(ii+1,N):
        x2 = XY[jj][1]
        y2 = XY[jj][0]
        xdiff = x2 - x1
        ydiff = y2 - y1
        t = gcd(xdiff, ydiff)
        error(xdiff, ydiff, t)
        xdiff = xdiff//t
        ydiff = ydiff//t
        error(xdiff, ydiff, t)
        s.add((xdiff,ydiff))
        s.add((-1*xdiff,-1*ydiff))

error(s)
print(len(s))

