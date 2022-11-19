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
n,l,r = map(int, input().split())
A = list(map(int, input().split()))

sumA = [0]*(n+1)
C = [0]*(n+1)
minC = [0]*(n+1)

for i in range(n):
    # 累積和を計算する
    sumA[i+1] = sumA[i] + A[i]
    # 左に着目した時に、左からi個を全てlに置き換えた場合にどれだけ小さくなるかの変化量の和を計算しておく
    C[i+1] = C[i] + (l - A[i])
    if minC[i] >= C[i+1]:
        minC[i+1] = C[i+1]
    else:
        minC[i+1] = minC[i]

ans = INF
# 全探索
for i in range(n+1):
    # i に着目する
    tmp = sumA[i]   # i 番目に着目 
    tmp += r*(n-i)  # i の右側を全て r に置き換えた場合
    tmp += minC[i]  # i 個を左から置き換えた場合の最小値(O(1)で求まるよう事前計算しておく)
    ans = min(ans, tmp)
print(ans)
    


