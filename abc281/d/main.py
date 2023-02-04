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

N,K,D=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
A=list(map(int, input().split()))  # (5)リストで受け取り 入力例:A1 A2 ... An

# dp[i][j][k]: i番目までみたときに、j個たしたときに余りがkになるもののうち最大の数
# 初期化
# 貰うDPでDPを更新する
# 選択する場合、選択しない場合に着目する

dp = [[[-INF]*(D) for _ in range(K+1)] for _ in range(N+1)]
# 初期化
dp[0][0][0] = 0

for ii in range(1,N+1):     # 1~N個まで順番にみていく
    aii = A[ii-1]
    for jj in range(K+1):   # 0~K個足している状態に着目する
        for kk in range(D):
            prev_kk = (kk-aii)%D
            # aiiを選択しない場合
            dp[ii][jj][kk] = dp[ii-1][jj][kk]
            # 選択する場合（少なくとも1個以上であることが条件）
            if jj != 0:
                # 貰うDP
                dp[ii][jj][kk] = max(dp[ii][jj][kk], dp[ii-1][jj-1][prev_kk] + aii)
ans = dp[N][K][0]
print(ans) if ans >= 0 else print(-1)
