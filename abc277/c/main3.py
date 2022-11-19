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

N=int(input())                     # (1)数字が1つ 入力例:N
d = defaultdict(list)

for ii in range(N):
    A, B = map(int, input().split())
    d[A].append(B)
    d[B].append(A)
#print(d)

visited = set()
dq = deque()
def bfs(sx):
    dq.append(sx)
    visited.add(sx)

    # bfs
    while dq:
        tx = dq.popleft()
        l = d[tx]
        for dx in l:
            if dx not in visited:
                dq.append(dx)
                visited.add(dx)
bfs(1)
print(max(visited))




