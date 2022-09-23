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
s = input()
t = input()

# table
dp = [ [0]*(len(s)+1) for ii in range(len(t)+1) ]

for jj in range(1, len(t)+1):
    for ii in range(1, len(s)+1):

        dp[jj][ii] = max(dp[jj][ii],
                         dp[jj][ii-1],
                         dp[jj-1][ii])
        if t[jj-1] == s[ii-1]:
            # 文字列が変わったところ
            dp[jj][ii] = max(dp[jj][ii],
                         dp[jj-1][ii-1]+1)

#print(dp[len(t)][len(s)])
#print(dp)
# 復元
#cnt = dp[len(t)][len(s)]
#ans = ""
#n = len(t) * len(s) - 1
#
ii = len(s)
jj = len(t)
ans = ''
while jj > 0 and ii > 0:
  if dp[jj][ii] == dp[jj][ii-1]:
    ii -= 1
  elif dp[jj][ii] == dp[jj-1][ii]:
    jj -= 1
  else:
    ans += s[ii-1]
    ii -= 1
    jj -= 1

print(ans[::-1])
