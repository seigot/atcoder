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
N,M=map(int, input().split()) 
gh = [[] for ii in range((N+2))]
for ii in range(M):
    x, y = map(int, input().split()) 
    gh[x].append(y)
#print(gh)


memo = [-1] * (N+1)

# グラフの深さを求める
def dfs(cx):

    # cacche
    if memo[cx] != -1:
        depth = memo[cx]
        return depth

    depth = 0
    # 枝に着目する
    for ii in range(len(gh[cx])):
        tx = gh[cx][ii]
        tmp = dfs(tx)
        depth = max(depth, tmp+1)
    memo[cx] = depth
    return depth

ans = 0
for ii in range(1, N+1):
    depth = dfs(ii)
    ans = max(ans, depth)
print(ans)

