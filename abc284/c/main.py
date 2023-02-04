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

# graph (N頂点M辺)
N,M=map(int, input().split())
gh = [[] for _ in range(N)] 
for ii in range(M):
    u,v=map(int, input().split())
    u -= 1
    v -= 1
    gh[u].append(v)
    gh[v].append(u)
#print(gh)

# 幅優先探索
svisit = set()
def bfs(n):
    q = deque()
    q.append(n)
    svisit.add(n)
    while q:
        tx = q.popleft()
        for dx in gh[tx]:
            if dx in svisit:
                # already visited
                continue
            # not visited
            q.append(dx)
            svisit.add(dx)

# 全頂点で探索
ans = 0
for ii in range(N):
    if ii in svisit:
        continue
    bfs(ii)
    ans += 1
print(ans)