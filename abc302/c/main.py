#!/usr/bin/env python3                                                                          
import sys
#input = sys.stdin.readline # 文字列Sの場合は最後に"¥n"が付くので注意
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

N,M=map(int, input().split())
l = []
for ii in range(N):
    S=input()
    l.append(S)

# 1.対象元文字列、比較対象文字列を決める
# 2.diffが1であるかどうかをチェックする
# 3.もしチェックOKであれば次の文字列をあげる
# 全て1.2.3が全部OKであればOK
def check_diff(s,t):
    cnt = 0
    for ii in range(len(s)):
        if s[ii] != t[ii]:
            cnt += 1
    return cnt

ps = permutations(l)
for ss in ps:
    error(ss)
    ans = 0
    for ii in range(N-1):
        if check_diff(ss[ii], ss[ii+1]) > 1:
            break
        ans += 1
    if ans >= N-1:
        error(N,M)
        print("Yes")
        exit()
error(N,M)
print("No")


