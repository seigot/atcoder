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

N = int(input())
l = []
for ii in range(N):
    S = input()
    l.append(list(S)) 

#   i-->
# j
# |  (i,j)
# v
ans = "No"
for jj in range(N):
    for ii in range(N):
        # 右
        if ii <= N-6:
            cnt = 0
            for kk in range(6):
                val = l[jj][ii+kk]
                if val == '#':
                    cnt+=1
            if cnt >= 4:
                ans = "Yes"

        # 右下
        if ii <= N-6 and jj <= N-6:
            cnt = 0
            for kk in range(6):
                val = l[jj+kk][ii+kk]
                if val == '#':
                    cnt+=1
            if cnt >= 4:
                ans = "Yes"

        # 下
        if jj <= N-6:
            cnt = 0
            for kk in range(6):
                val = l[jj+kk][ii]
                if val == '#':
                    cnt+=1
            if cnt >= 4:
                ans = "Yes"

        # 左下
        if 5 <= ii and jj <= N-6:
            cnt = 0
            for kk in range(6):
                val = l[jj+kk][ii-kk]
                if val == '#':
                    cnt+=1
            if cnt >= 4:
                ans = "Yes"

# print(l[2][1]) #
print(ans)