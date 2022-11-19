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

# 項数が N の正整数列 A=(a1 ,…,a N ) が与えられます。
# A の項を 1 個以上選ぶ方法は 2 N −1 通りありますが、
# そのうち選んだ項の平均値が整数であるものが何通りかを 998244353 で割った余りを求めてください。
n = int(input())
A = list(map(int, input().split()))

def solve(x):
    # 初期化
    # [j][k] j個選んだ時の総和がmod x でkのやつの数
    dp = [[0]*x for _ in range(n+1)]
    dp[0][0] = 1
    # 全要素について探索する
    for i in range(n):
        a = A[i]
        # dpを再計算する
        for j in range(i,-1,-1):
            #print(j)
            for k in range(x):
                # 前回の余りがkになるものの数ぶんループをまわす
                # 前回余りがkになったものにaを足した時の余りをdpにいれる
                dp[j+1][(k+a)%x] += dp[j][k]
                dp[j+1][(k+a)%x] %= MOD
        # print(dp)
    return dp[x][0]
ans = 0

for i in range(1,n+1):
    # 1つ選んだ場合, 2つ選んだ場合、、iつ選んだ場合をdpで求めていく。
    # それぞれの数を選んだ場合のうち、余りが0になるものの和が答え
    ans += solve(i)
    ans %= MOD
    
print(ans)
