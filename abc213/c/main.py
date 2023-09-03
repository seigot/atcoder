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

H,W,N=map(int, input().split())
Xlist = []
Ylist = []
Xdict = defaultdict(int)
Ydict = defaultdict(int)
for ii in range(N):
    x, y = map(int, input().split())
    Xlist.append(x)
    Ylist.append(y)
_Xlist = sorted(list(set(Xlist)))
_Ylist = sorted(list(set(Ylist)))
for i,v in enumerate(_Xlist):
    Xdict[v] = i + 1
for i,v in enumerate(_Ylist):
    Ydict[v] = i + 1
for ii in range(N):
    x =Xdict[Xlist[ii]]
    y =Ydict[Ylist[ii]]
    print(x,y)