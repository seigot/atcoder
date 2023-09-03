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

W,H=map(int, input().split())
N=int(input())
pq=[list(map(int, input().split())) for n in range(N)]
A=int(input())
a=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
B=int(input())
b=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An


dictPiece = defaultdict(int)
maxv = 0
for ii in range(N):
    p,q = pq[ii]
    pp = bisect_left(a,p)
    qq = bisect_left(b,q)
    dictPiece[qq*(A+1)+pp] += 1
minv = 0
num = len(dictPiece.keys())
if num == (A+1)*(B+1):
    minv = min(dictPiece.values())
maxv = max(dictPiece.values())
print(minv,maxv)
