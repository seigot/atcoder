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
H, W = map(int, input().split())
C = [input() for ii in range(H)]
#print(C)

ans = [0] * W
# 横
for ii in range(W):
    # 縦
    cnt = 0
    for jj in range(H):
        c = C[jj][ii]
        if c == '#':
            cnt += 1

    ans[ii] = cnt
print(*ans)
