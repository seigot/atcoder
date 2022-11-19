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
# 3 5   N,M
# 1 3   A1, B1
# 1 4   A2, B2
# 2 5   A3, A3
# ...

# 尺取り法/いもす法を使って数を求めていく
N, M = map(int, input().split())
pairs = [[] for _ in range(M+1)]  # Aのpair用
r = 0     # 右端
minB = M
for i in range(N):
    A, B = map(int, input().split())
    pairs[A].append(B)
    r = max(r, A)                 # rは少なくともmax(r, A)以上であるのでこれを基準にする
    minB = min(minB, B)           # 少なくともminBまでは探索が必要なのでこれを基準にする

f = [0] * (M+10)                  # f(k)の値
for l in range(1, minB+1):        # lは1〜minBまで探索する
    f[r-l+1] += 1                 # [l,r]に着目した時の長さをカウントする
    f[M-l+1 + 1] -= 1             # 
    if pairs[l] == []:            # rを更新する。pairs[l]が
        continue
    else:
        r = max(r, max(pairs[l]))

for i in range(1, M+1):
    f[i] += f[i-1]
    print(f[i])
    
    
    

