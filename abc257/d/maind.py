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

n = int(input())
l = []
# ジャンプ台の座標とパワー
for _ in range(n):
    x, y, p = map(int, input().split())
    l.append((x, y, p))
# 距離(iからjまでの距離を二次元配列で管理)
d = [[0] * n for _ in range(n)]

# 距離を全探索
for i in range(n):
    for j in range(n):
        x1, y1, p = l[i]
        x2, y2, _ = l[j]
        dist = abs(x1 - x2) + abs(y1 - y2)
        d[i][j] = 0 - -dist // p

# ワーシャルフロイド法
for k in range(n):
    for i in range(n):
        for j in range(n):
            d[i][j] = min(d[i][j], max(d[i][k], d[k][j]))

ans = 10**10
for i in range(n):
    ans = min(ans, max(d[i]))
print(ans)

