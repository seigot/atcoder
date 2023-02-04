#!/usr/bin/env python3
import sys
sys.setrecursionlimit(4100000)
import math
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict, deque
dpos4 = ((1, 0), (0, 1), (-1, 0), (0, -1))
dpos8 = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N,A,B=map(int, input().split())
S=list(input())

N = len(S)
# 全探索
# pattern1: 全ての文字を置き換える
# pattern2: rotateで回文を作成する

ans = B * N # pattern1
S2 = S + S
for offset in range(N): # pattern2 (0~N-1回ずらすことを想定)
    # ii回ずらした時に回文を作るためのコスト
    cost = A * offset
    for ti in range(N//2):
        idx = offset + ti
        idx2 = offset + N - 1 - (ti)
        if S2[idx] != S2[idx2]:
            cost += B
    ans = min(ans,cost)

print(ans)
