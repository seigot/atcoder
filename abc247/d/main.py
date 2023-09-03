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

Q=int(input())
query = [list(map(int,input().split())) for _ in range(Q)]
error(query)
dq = deque()
for ii in range(Q):
    error(dq)
    q = query[ii]
    if q[0] == 1:
        x = q[1]
        c = q[2]
        # 筒に追加
        dq.append((x,c))
    if q[0] == 2:
        c = q[1]
        sum = 0
        # 筒から取得
        while True:
            tx,tc = dq.popleft()
            if tc >= c:
                # 全て取り除く
                sum += tx*c
                tc -= c
                if tc != 0:
                    # 余りは筒に戻す
                    dq.appendleft((tx,tc))
                break
            else: # tc < c:
                sum += tx*tc
                c -= tc             
        print(sum)
