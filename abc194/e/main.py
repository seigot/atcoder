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

N,M = map(int,input().split())
A = list(map(int,input().split()))
data = [0]*(N+1)

# 頻度に着目する、最初に区間(M)に出現する数の頻度を取得する
for i in range(M):
    data[A[i]] += 1
# 0~始まりで頻度が0のものが最小の非負整数
for i in range(N+1):
    if data[i] == 0:
        mex = i
        break
# 区間をずらして頻度を計算していく
for i in range(1, N-M+1):
    data[A[i-1]] -= 1
    data[A[i+M-1]] += 1
    # 頻度を減算した際に0になったものがある場合、それが最小の非負整数である
    if data[A[i-1]] == 0:
        mex = min(mex, A[i-1])
print(mex)
