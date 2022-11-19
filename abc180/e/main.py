#!/usr/bin/env python3
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
# https://atcoder.jp/contests/abc180/submissions/17458763

# 入力
n = int(input())
points = [tuple(map(int,input().split())) for _ in range(n)]

# 距離を計算する(各jから各iまでの全ての組み合わせの距離を事前に計算する)
def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + max(b[2] - a[2], 0)
dist = [[distance(points[j], points[i]) for i in range(n)] for j in range(n)]
#print(dist)

#dp[1<<n][n]
#dp[かつてどこ通ったか][いま]
#いま in かつてどこ通ったか
dp = [[INF] * n for _ in range(2**n)] #かつてどこ通ったかはbitで管理するので2**n個の配列が要る

# 最初は0
#dp[1][0] = 0
dp[0][0] = 0
# オーダ(2**n * n * n)
for bit in range(0, 2**n, 2):      # かつてどこ通ったかのbitを立てる
    for now in range(n):     # 現在(これまでnowに至るまで通ってきた道のうち最小の道)
        for nxt in range(n): # 次(現在から次に通る道に着目する)
            # コストが低い道が見つかった場合は更新する
            # 現在のnowを経由した方がコストが低ければ更新する的な感じ
            dp[bit | (2**nxt)][nxt] = min(dp[bit | (2**nxt)][nxt],        # 対象 --> nxt
                                          dp[bit][now] + dist[now][nxt])  # 対象 --> now --> nxt
#            dp[bit][nxt] = min(dp[bit][nxt], dp[bit][now] + dist[now][nxt])

#print(dp)
# dp[]の最後に戻ってくるルート(i-->0)を足して最小値を出力する
print(min(dp[(1 << n)-1][i] + dist[i][0] for i in range(n)))
