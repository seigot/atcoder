#https://atcoder.jp/contests/ABC253/submissions/32067628

#dp[i][j] := i番目まで見たとき、最後がjの通り数
#dp[i+1][k] = dp[i][j]
#j 1～M
#k 1～j-K, j+K～M
#3重ループだと10**9 累積
#sdp[i] 
import sys
sys.setrecursionlimit(4100000)
import math
import itertools
import collections
from heapq import heapify, heappop, heappush
from bisect import bisect, bisect_left, bisect_right
def error(*args, end="\n"): print("[stderr]", *args, end=end, file=sys.stderr)
def YesNo(flag: bool, yes="Yes", no="No"): print(yes) if flag else print(no)
from collections import defaultdict, deque
MOD = 998244353
INF = float("inf")
MINF = -float("inf")

N, M, K = map(int,input().split())
MOD = 998244353
 
# init
# 長さiで最後がjなやつの個数
dp = [[0]*(M+1) for _ in range(N+1)]
acc = [0]*(M+1)
# 初めは全て1通り存在する(ただし0は存在しない)
for i in range(M):
    dp[0][i+1] = 1

error("dp",dp)

for i in range(1,N): # 1~N-1まで配列を回す

    for j in range(1,M+1): # 1~Mまでの場合の数を求める(0は存在しない)
        acc[j] = acc[j-1] + dp[i-1][j] 
        #acc[i] := dp[i-1][1] + dp[i-1][2] + ,,,
    error("acc", acc)

    # これまでの値から、i項目がjで終わる場合の数を求める
    # jは1~Mまでの制約がある
    for j in range(1,M+1):
        # 上の部分
        if 0 < j+K-1 <= M:
            # 累積和で上の部分を求める（差分で求める）
            dp[i][j] += acc[M]
            dp[i][j] %= MOD
            dp[i][j] -= acc[j+K-1]
            dp[i][j] %= MOD
        # 下の部分
        if j - K > 0:
            # 累積和で下の部分を求める（ここは普通）
            dp[i][j] += acc[j-K]
            dp[i][j] %= MOD
    error("dp", dp)

ans = 0
error("N-1", N-1)
# N項目が1~Mで終わる場合の数を合計する
for j in range(1,M+1):
    ans += dp[N-1][j]
    error("ans", ans)
    ans %= MOD

print(ans)