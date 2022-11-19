#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
S = []
for ii in range(10):
    Sn = input()
    S.append(Sn)
# print(S)

# init
N = 10
A = -1 # 縦
B = -1 # 縦
C = -1 # 横
D = -1 # 横

# 縦を操作する
for ii in range(N):
    for jj in range(N):
        c = S[jj][ii]
        if c == '#':
            if A == -1:
                A = jj
            B = jj

# 横を操作する
for jj in range(N):
    for ii in range(N):
        c = S[jj][ii]
        if c == '#':
            if C == -1:
                C = ii
            D = ii

print(A+1, B+1)
print(C+1, D+1)



