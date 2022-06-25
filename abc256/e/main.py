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

N = int(input())
X = [-1] + list(map(int, input().split()))
C = [-1] + list(map(int, input().split()))

visited = [False] * (N+1)
tmp_visited = [False] * (N+1)
ans = 0

# ノードiiに着目して深さ優先探索する
def check(ii):
    global ans
    if visited[ii] == True:
        return
    if tmp_visited[ii] == True:
        # ループ検出
        # 次のノードから探索する
        tx = X[ii]
        cost = C[ii]
        while tx != ii:
            # ループ中の最小コスト検出
            tx = X[tx]
            cost = min(cost, C[tx])
        # 最小コストは除いてもOK
        ans += cost
        return 
    tmp_visited[ii] = True
    check(X[ii])
    # 訪れたノードは全て印をつける
    visited[ii] = True

for ii in range(1, N+1):
    check(ii)

print(ans)