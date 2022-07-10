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
N, K, Q = map(int, input().split())
A = list(map(int, input().split())) # コマ
L = list(map(int, input().split())) # 操作

# マス N
# コマ数 K
# 操作数 Q

for ii in range(len(L)):
    # ターゲットの番号
    t_idx = L[ii]
    t_idx -= 1

    # ターゲットが右端にいるかどうか
    if A[t_idx] == N:
        continue
    # ターゲットの右にコマがいるかどうか(右端のコマ以外)
    if t_idx != K-1 and A[t_idx] + 1 == A[t_idx+1]:
        continue
    # 移動
    A[t_idx] = A[t_idx] + 1
print(*A)


