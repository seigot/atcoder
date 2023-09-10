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

N,M=map(int, input().split())
L=list(map(int, input().split()))

# 横幅がwの時、何行に収まるか
def check_l(w):

    line = 1
    cnt = 0
    flg = True
    for ii,lenl in enumerate(L):
        if lenl > w:
            flg = False
        # 追加
        if cnt + lenl <= w:
            cnt += lenl
        else:
            line += 1
            cnt = lenl
        cnt+=1
    return line,flg

upper = 10**16
#lowwer = max(L)-1
lowwer = 0
while upper-lowwer>1:
#for ii in range(60):
    middle = (lowwer+upper)//2
    line,flg = check_l(middle)
    if line <= M and flg == True:
        upper = middle
    else:
        lowwer = middle
print(upper)

