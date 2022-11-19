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


# N(カードの数), S(総和)
# dp[i][j]:   i番目までめくった際に総和がjになるかどうか   なる:True, ならない:False
#     i <= 100
#     ai,bi <= 100
#     j <= 10000
#
# H:表、T:裏

N,S=map(int, input().split())
an = []
for ii in range(N):
    a, b =map(int, input().split())
    an.append((a,b))
#print(an)

JMAX=1000000+1
#JMAX=41
dp = [[0]*JMAX for ii in range(N+1)]

# 全てのカードについて表裏の組み合わせを考える
for ii in range(N):

    Hn = an[ii][0]
    Tn = an[ii][1]
    if ii == 0:
        dp[ii][Hn] = 1
        dp[ii][Tn] = 1
    else:
        for jj in range(JMAX):
            if dp[ii-1][jj] == 1:
                dp[ii][jj + Hn] = 1
                dp[ii][jj + Tn] = 1
#print(dp)
#print(dp[N-1][S])

if dp[N-1][S] == 0:
    print("No")
    exit(0)
else:
    print("Yes")

# 解の復元
# True -->H,TどちらかのTrueを辿れば求まる
#ans = []
ans = ""
ti = N-1
tj = S
for ii in range(N-1, -1, -1):
    ti = ii
#    print(ti,tj,dp[ti][tj])
    # 1つ前がTrueのやつを探す
    ann = []
    ann.append(an[ti][0]) # H
    ann.append(an[ti][1]) # T
    if ti == 0:
        if dp[ti][tj] == True:
            if tj == ann[0]:
                ans += "H"
            else:
                ans += "T"
#            ans.append(tj)
        break
    for jj in ann:
        if dp[ti-1][tj-jj] == True:
            tj = tj-jj
#            print(jj)
#            ans.append(jj)
            if jj == ann[0]:
                ans += "H"
            else:
                ans += "T"
            break
#print(ans)
print(ans[::-1])
#ans_c = ""
#for ii in ans[::-1]:
