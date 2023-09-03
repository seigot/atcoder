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

A.sort()
B.sort()
sizeB = len(B)
error(A)
error(B)

l = 0
r = 10**10

cnt = 0
while r - l > 1:
    c = (r + l) // 2 
    bA = bisect_left(A, c)
    bB = bisect_left(B, c)
    numA = bA
    numB = sizeB - bB
    error(c)
    error(bA,bB)
    error(numA,numB)
    if numA >= numB:
        r = c
    else:
        l = c
    cnt += 1
    if cnt == 40:
#        exit()
        pass

error(l,r)
#print(l)
#exit()
bA = bisect_right(A, l)
bB = bisect_left(B, l)
numA = bA
numB = sizeB - bB
error(numA,numB)
if numA >= numB:
    print(l)
else:
    print(r)