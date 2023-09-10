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

#https://atcoder.jp/contests/ABC319/tasks/ABC319_d 
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd


n,m = map(int,input().split())
a = list(map(int,input().split()))
mx = max(a)
#l = mx-1
l = 0
r = 10**16
for i in range(60):
    md = (l+r)//2
    now = 1
    row = 0
    ok = 1
    for i in range(n):
        if a[i] > md:
            ok = 0
        if row + a[i] <= md:
            row += a[i]
        else:
            now += 1
            row = a[i]
        row += 1
    if now <= m and ok:
        r = md
    else:
        l = md
print(r)