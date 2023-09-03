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

N=int(input())
A=list(map(int, input().split()))
Q=int(input())
LR=[list(map(int, input().split())) for q in range(Q)]
error(LR)

# 累積和
sleep_time = [] # 睡眠開始時間の配列
sleep_sum = [] # 区間毎の睡眠時間
sleep_cum = [] # 区間毎の睡眠時間の累積和
s = set(A)
for ii in range(1,N):
    if ii % 2 == 1: # 睡眠開始時間
        sleep_time.append(A[ii])
        pre = A[ii]
    else: # 起床
        sleep_hour = A[ii] - pre
        sleep_sum.append(sleep_hour)
sleep_cum.append(0)
for ii in range(len(sleep_sum)):
    sum = sleep_sum[ii]+sleep_cum[-1]
    sleep_cum.append(sum)

def f(v):
    bi = bisect_left(sleep_time, v)
    if bi == 0:
        return 0
    base = sleep_cum[bi - 1]
    diff = min(v - sleep_time[bi - 1],
                sleep_sum[bi - 1])
    return base + diff

# 答えを求める
for ii in range(Q):
    l = LR[ii][0]
    r = LR[ii][1]
    ans = f(r) - f(l)
    print(ans)
