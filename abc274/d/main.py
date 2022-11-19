#!/usr/bin/env python3
from locale import ABDAY_1
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

# A,B=map(int, input().split())      # (2)数字が2つ以上で別々に受け取り  入力例:A B
N, x, y=map(int, input().split()) 
A = list(map(int, input().split()))

# p1 = (0,0)
# p2 = (Ai,0)
# pN = (Ax,0)
# pN+1 = (x,y)
# 点 piと点 pi+1の距離はAi(1≤i≤N)
# 線分pi pi+1 と線分pi+1 pi+2のなす角は 90 度 (1≤i≤N−1)

Aeven = [] # 偶数
Aodd = []  # 奇数
for ii in range(N):
    a = A[ii]
    if ii%2 == 0:        
        Aeven.append(a)
    else:
        Aodd.append(a)

# 横方向 / 偶数
dp = [set() for ii in range(((N+1)//2))]  
dp[0].add(Aeven[0])
for ii in range(1, len(Aeven)):
    a = Aeven[ii]
    for AA in dp[ii-1]:
        dp[ii].add(AA + a)
        dp[ii].add(AA - a)

if x in set(dp[-1]):
    ans1 = "Yes"
else:
    ans1 = "No"

# 縦方向 / 奇数
dp2 = [set() for ii in range((N//2))] 
dp2[0].add(Aodd[0])
dp2[0].add(Aodd[0]*(-1))
for ii in range(1, len(Aodd)):
    a = Aodd[ii]
    for AA in dp2[ii-1]:
        dp2[ii].add(AA + a)
        dp2[ii].add(AA - a)

if y in set(dp2[-1]):
    ans2 = "Yes"
else:
    ans2 = "No"

if ans1 == "Yes" and ans2 == "Yes":
    print("Yes")
else:
    print("No")
