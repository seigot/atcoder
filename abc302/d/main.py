#!/usr/bin/env python3                                                                          
import sys
input = sys.stdin.readline # 文字列Sの場合は最後に"¥n"が付くので注意
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

N,M,D=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
#A.append(MINF)
B.append(MINF)
B.append(INF)
B.append(INF)
_A = sorted(A)
_B = sorted(B)
error(_A)
error(_B)

# Aの先頭から順に探索する
# A以上となる部分をBから二分探索してその差をみる
def check(val,a,d):
    if a - d  <= val and val <= a + d:
        return True 
    return False

ans = -1
for a in _A:
    # minus
    idx = bisect_left(_B,a-D)
    for ii in range(idx-1,idx+2):
        if check(_B[ii],a,D) == True:
            ans = max(ans, a+_B[ii])
    # plus
    idx = bisect_left(_B,a+D)
    for ii in range(idx-1,idx+2):
        if check(_B[ii],a,D) == True:
            ans = max(ans, a+_B[ii])

print(ans)
