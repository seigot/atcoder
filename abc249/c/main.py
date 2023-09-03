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

N,K=map(int, input().split())
S = []

def s2bit(s):
    d = defaultdict(int)
    for c in s:
        d[c] = 1
    b = ""
    for c in "abcdefghijklmnopqrstuvwxyz":
        b = b + str(d[c])
    return b

for ii in range(N):
    s = input()
    s2 = s2bit(s)
    S.append(s2)
error(S)

ans = 0
for ii in range(1,1<<N):
    # select
    error("----",ii)
    ll = []
    cnt = 0
    for jj in range(N):
        if (ii>>jj)&1 == 1:
            ll.append(S[jj])
            cnt += 1
    error(ll)
    # check
    cnt2 = 0
    for jj in range(len("abcdefghijklmnopqrstuvwxyz")):
        cnt3 = 0
        for kk in range(cnt):
            if ll[kk][jj] == "1":
                cnt3 += 1
        if cnt3 == K:
            cnt2 += 1
    error(cnt2)
    ans = max(ans,cnt2)
print(ans)
