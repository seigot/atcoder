#!/usr/bin/env python3                                                                          
import sys
#input = sys.stdin.readline().rstrip() # 文字列Sの場合は最後に"¥n"が付くので注意
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

N,M,H,K=map(int, input().split())
S=input()
xy = set()
for ii in range(M):
    x,y=map(int, input().split())
    xy.add((x,y))

HP = H
tx = 0
ty = 0
for s in S:
    if s == "R":
        tx += 1
        ty += 0
    if s == "L":
        tx -= 1
        ty += 0
    if s == "U":
        tx += 0
        ty += 1
    if s == "D":
        tx += 0
        ty -= 1
    HP -= 1
    if HP < 0:
        print("No")
        exit()
    if HP < K and (tx,ty) in xy:
        xy.discard((tx,ty))
        HP = K
print("Yes")