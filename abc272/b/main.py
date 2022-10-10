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
N, M=map(int, input().split())
kx = []
for ii in range(M):
    k = list(map(int, input().split()))
    kx.append(k)

# ペアになったかどうか判定用の配列
mat = [[0]*N for ii in range(N)]
#print(mat)
# 全探索
for ii in range(M):
    k = kx[ii]
    # ペアになった人を配列に入れる
    for jj in range(1, len(k)):
        t1 = k[jj]
        for kk in range(1, len(k)):
            t2 = k[kk]
            mat[t1-1][t2-1] = 1
    #print(mat)

num = 0
for ii in range(N):
    num += sum(mat[ii])
#print(num)
if num == N*N:
    print("Yes")
else:
    print("No")
