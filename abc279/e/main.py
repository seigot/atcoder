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

N,M=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An
B=[ii for ii in range(N+1)]        # 0-indexed
#print(B)


# 先頭から順番に数字を並び替える
d_change = defaultdict(int)
for ii in range(M):
    # target index
    tidx = A[ii]
    # 入れ替え
    d_change[ii] = (B[tidx], B[tidx+1]) # memo
    tmp = B[tidx]
    B[tidx] = B[tidx+1]
    B[tidx+1] = tmp
#print(B)
#print(d_change)

# 数値のindexを記録
d = defaultdict(int)
for ii in range(len(B)):
    d[B[ii]] = ii
#print(d)

# 各iiにおいて所定の所作を行った際の1のindexを出力する
for ii in range(M):
    tidx = ii
    t = d_change[ii]
    if t[0] == 1:
        tidx = t[1]
    elif t[1] == 1:
        tidx = t[0]
    else:
        tidx = 1
    print(d[tidx])