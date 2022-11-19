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
H,W=map(int, input().split())
G = [input() for _ in range(H)]

#print(G)
#print(G[0][2])

# 探索
dq = deque()
dq.append((0,0))
visited = set()
visited.add((0,0))
while True:
    ty,tx = dq.popleft()
    c = G[ty][tx]
    dx = 0
    dy = 0
    if c == "U":
        dy = -1
    elif c == "D":
        dy = 1
    elif c == "L":
        dx = -1
    elif c == "R":
        dx = 1
    nx = tx + dx
    ny = ty + dy
    if (ny, nx) in visited:
        # loop
        print(-1)
        exit(0)
    elif 0 <= nx < W and 0 <= ny < H:
        visited.add((ny, nx))
        dq.append((ny, nx))
    else:
        break
print(ty+1, tx+1)
