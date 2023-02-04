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

MOD = 998244353

#modinv = lambda x:pow(x, -1, MOD) # 逆元を求める。python3.8であればOK
modinv = lambda x:pow(x, MOD - 2, MOD) # 逆元を求める。pypyの場合はこちらを使う

N,P = map(int,input().split())

# dp[i]: 体力iを0にするために必要な回数の期待値
DP = [0] * (N + 1)
DP[0] = 0
DP[1] = 1

for n in range(2, N + 1):
    wk = 0
    wk += P * modinv(100) * (DP[n - 2] + 1)
    wk += (100 - P) * modinv(100) * (DP[n - 1] + 1)
    DP[n] = wk % MOD
    
print(DP[N])
