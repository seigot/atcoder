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

#https://atcoder.jp/contests/ABC319/tasks/ABC319_e 
import sys
sys.setrecursionlimit(5*10**5)
input = sys.stdin.readline
from collections import defaultdict, deque, Counter
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
from math import gcd


n,x,y = map(int,input().split())
pt = [list(map(int,input().split())) for i in range(n-1)]

ans = []

# aの倍数でb以上の数
def f(a, b):
    x = ((b - 1) // a + 1) * a
    return x
print(f(25,50)) # 50

# 周期処理を求める(Max840=lcm(1,2,3,4,5,6,7,8))
for j in range(840):
    nt = j+x
    for i in range(n-1):
        pi,ti = pt[i]
        nt = f(pi, nt) + ti
    nt += y
    ans.append(nt)

q = int(input())
for _ in range(q):
    qi = int(input())
    ansi = INF
    p, mod = divmod(qi, 840)
    print(ans[mod] + p * 840) 
