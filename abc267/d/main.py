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

N,M = map(int, input().split()) 
A = list(map(int, input().split()))

# dp[i][j]:= 
# Aiまでのうち、すでに j個の要素を Bの要素として選んだときのk=1∑jk×Bk の最大値
# dp[i][j] = max(dp[i−1][j], dp[i−1][j−1]+j×Ai)

dp = [ [-INF]*(N+1) for ii in range(N+1) ]
#print(dp) 

# init
dp[0][0]=0
# 先頭から選択していく
# iが今着目している番号（1~N個目）
#for i in range(1,N+1):
#    # i番目に着目した時、j(0indexなので実際はj+1)個選んだ最大値を更新していく（漸化式）
#    for j in range(min(i+1,M+1)):
#        dp[i][j]=max(dp[i-1][j],            # 今の値を選択しない
#                     dp[i-1][j-1]+A[i-1]*j) # 今の値を選択する（代わりに）
for i in range(N):
    # i番目に着目した時、j(0indexなので実際はj+1)個選んだ最大値を更新していく（漸化式）
    for j in range(min(i+2,M+1)):
        dp[i+1][j]=max(dp[i][j],            # 今の値を選択しない
                       dp[i][j-1]+A[i]*j)   # 今の値を選択する（代わりに）

print(dp[N][M])


