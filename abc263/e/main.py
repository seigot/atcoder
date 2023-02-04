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


modinv = lambda x:pow(x, MOD - 2, MOD)

n=int(input())
a=[0]+list(map(int,input().split()))

# Pi =マスiに到達する確率
p=[0]*(n+2)
p[1]=1
p[2]=-1
# 配るDPで求める
for i in range(1,n):
    p[i] += p[i-1]
    p[i+1] += p[i]*modinv(a[i])%MOD
    p[i+a[i]+1] -= p[i]*modinv(a[i])%MOD

# サイコロを振る回数の期待値
# ∑ i=1 n−1 ((Ai+1)/Ai)*Pi
ans=0
for i in range(1,n):
    ans+=p[i]*(a[i]+1)*modinv(a[i])
print(ans%MOD)

