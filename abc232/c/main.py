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

import itertools
n,m = map(int,input().split())
graph1 = [[] for i in range(n+1)] # takahashi
graph2 = [[] for i in range(n+1)] # sunuke
for i in range(m):
    a,b = map(int,input().split())
    graph1[a].append(b)
    graph1[b].append(a)
for i in range(m):
    a,b = map(int,input().split())
    graph2[a].append(b)
    graph2[b].append(a)
x = [i+1 for i in range(n)]
xx = itertools.permutations(x)
error(xx)
error(graph1)
error(graph2)
for pattern in xx:
    error(pattern)
    flag = True
    # x-->yが該当すると仮定した場合に、同じグラフとなるかどうかを確認する
    # これを全探索する(n=最大8なので計算時間は間に合う)
    for i in range(1,n+1):         
        ######
        # permutationのpatternのi番目に着目する
        # i=1~n
        ######
        for graph1_n in graph1[i]:
            # graph1(takahashi)の[i]に繋がっているものたちが、
            # pare候補(pare)と繋がっているかどうかをチェックする
            pare = pattern[i-1]
            # graph1_nはpare候補でいうところのpare_nxt番なので変換する
            pare_nxt = pattern[graph1_n-1]
            error(pare, pare_nxt)
            if pare_nxt not in graph2[pare]:
                # pare候補(pare)にpare_nxt番(上記で変換したiに対応するもの)が含まれていない場合は諦める
                flag = False
                break
        if flag == False:
            break
    if flag:
        print('Yes')
        break
else:
    print('No')