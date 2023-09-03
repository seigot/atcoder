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

N,M=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))

s = set()
s2 = set()
A.sort()
B.sort()
#B.sort(reverse=True)
sizeB = len(B)
s |= set(A)
s |= set(B)
for v in s:
    s2.add(v)
    s2.add(v+1)
s3 = sorted(s2)

error(A)
error(B)
error(s)
error(s2)
error(s3)

for v in s3:
    iA = bisect_right(A,v)
    iB = bisect_left(B,v)
#    iB = bisect_right(B,v)
    numA = iA
#    numB = iB
    numB = sizeB - iB
    if numA >= numB:
        print(v)
        exit()

